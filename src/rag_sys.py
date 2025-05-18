import ollama
import xml.etree.ElementTree as ET
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
import re

# === CONFIGURATION ===
EMBEDDING_MODEL = 'nomic-embed-text'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

VECTOR_DB = []
DESCRIPTIONS = []

# Load the dataset
dataset = []
tree = ET.parse('rag_system/resources/dataset.xml')
root = tree.getroot()
skip_task = 13 # for evaluation example set need to exclude from the RAG system

for sample in root.findall('Sample'):
    index = sample.find('Index').text
    description_element = sample.find('Description')
    description = description_element.text if description_element is not None and description_element.text is not None else 'Empty'

    python_code_element = sample.find('PythonCode')
    python_code = python_code_element.text if python_code_element is not None else None

    try:
        # Load Python files
        with open(f'rag_system/resources/pythoncodes/{index}_generated_sim.py', 'r') as file:
            content = file.read()
            if python_code is None:
                python_code = content
    except FileNotFoundError:
        print(f"Error: The file '{index}' was not found.")

    # Skip the task if the index matches the skip_task value
    if int(index) == skip_task:
        description = 'Empty'
        python_code = ''
        print(f"Skipping task with index {index} for evaluation example set.")

    dataset.append({'Index': index, 'Description': description, 'PythonCode': python_code})
    DESCRIPTIONS.append(description)

print(f'Loaded {len(dataset)} entries')

# === CREATE BM25 INDEX ===
tokenized_descriptions = [desc.lower().split() for desc in DESCRIPTIONS]
bm25 = BM25Okapi(tokenized_descriptions)


def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk, options={'num-ctx': 4096})['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))
    return np.array(embedding)


embeddings = []

for i, chunk in enumerate(dataset):
    desc = chunk['Description']
    emd = add_chunk_to_database(desc)
    embeddings.append(emd)
    print(f'Added chunk {i + 1}/{len(dataset)} to the database')

embeddings = np.array(embeddings)
dim = embeddings.shape[1]
faiss_index = faiss.IndexFlatL2(dim)
faiss_index.add(embeddings)

print("Vector Database Initialized.")
print(f"Total {len(VECTOR_DB)} descriptions embedded.")
print("✅ Vector Database is ready for retrieval!")

# === RETRIEVAL FUNCTIONS ===
def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = sum([x ** 2 for x in a]) ** 0.5
    norm_b = sum([x ** 2 for x in b]) ** 0.5
    return dot_product / (norm_a * norm_b)


def bm25_search(query, top_n=3):
    tokenized_query = query.lower().split()
    scores = bm25.get_scores(tokenized_query)
    top_indices = np.argsort(scores)[::-1][:top_n]
    return [(DESCRIPTIONS[i], scores[i]) for i in top_indices]


def vector_search(query, top_n=3):
    query_embedding = add_chunk_to_database(query).reshape(1, -1)
    _, indices = faiss_index.search(query_embedding, top_n)
    return [DESCRIPTIONS[i] for i in indices[0]]


def extract_indices(text):
    """
    Extracts index numbers from a given text containing '--Index <number> DESCRIPTION--' patterns.

    :param text: The input string containing index patterns.
    :return: A list of extracted index numbers as integers.
    """
    pattern = r"--Index (\d+)"
    indices = re.findall(pattern, text)
    if (len(indices) == 0):
        indices = re.findall(r"\d+", text)  # Find all numeric values
    if len(indices) == 0:
        return []
    return list(map(int, indices))  # Convert to integers


def rerank_results(query, results):
    prompt = (f"Query: {query}\n\nRank the most relevant descriptions for this query. "
              f"Please provide only description index order from most relevant to least relevant as output without "
              f"any other text( like 3,2,4):\n\n")
    for i, result in enumerate(results):
        prompt += f"\n--Index {result}  DESCRIPTION-- \n{DESCRIPTIONS[result]}\n --END DESCRIPTION-- \n"

    response = ollama.chat(model=LANGUAGE_MODEL, messages=[{"role": "user", "content": prompt}])
    index = extract_indices(response["message"]["content"])

    if len(index) == 0:
        return None
    # Check if all input result indices are present in the extracted indices
    if not all(result in index for result in results):
        return None

    return index


def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    # temporary list to store (chunk, similarity) pairs
    similarities = [(index, chunk, cosine_similarity(query_embedding, embedding)) for index, (chunk, embedding) in
                    enumerate(VECTOR_DB)]

    # sort by similarity in descending order, because higher similarity means more relevant chunks
    similarities.sort(key=lambda x: x[2], reverse=True)
    # finally, return the top N most relevant chunks
    return similarities[:top_n]


def hybrid_retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]

    # BM25 retrieval
    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)

    # Embedding-based retrieval
    similarities = []
    for i, (chunk, embedding) in enumerate(VECTOR_DB):
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((i, chunk, similarity))

    # Combine BM25 and embedding scores
    combined_scores = [(i, bm25_scores[i] + similarities[i][2]) for i in range(len(bm25_scores))]
    combined_scores.sort(key=lambda x: x[1], reverse=True)

    # Retrieve top N results
    top_indices = [index for index, score in combined_scores[:top_n]]
    best_match = rerank_results(query, top_indices)
    # Handle the case when rerank_results returns None (no valid indices provided)
    if best_match is None:
        return [(index, chunk, score) for index, chunk, score in similarities if index in top_indices]
    else:
        return [(index, chunk, score) for index, chunk, score in similarities if index in best_match]


def get_retrieved_details1(query, is_direct=True):
    if is_direct:
        retrieved_knowledge = retrieve(query)
    else:
        retrieved_knowledge = hybrid_retrieve(query)
    details = [{'Description': chunk, 'PythonCode': dataset[index]['PythonCode']} for index, chunk, _ in
               retrieved_knowledge]
    return details
