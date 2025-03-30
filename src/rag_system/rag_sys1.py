import ollama
import xml.etree.ElementTree as ET
import faiss
import numpy as np
from rank_bm25 import BM25Okapi

# === CONFIGURATION ===
# EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-large-en-v1.5-gguf'
EMBEDDING_MODEL = 'nomic-embed-text'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []
DESCRIPTIONS = []  # Stores descriptions for BM25


dataset = []
tree = ET.parse('resources/dataset.xml')
root = tree.getroot()
for sample in root.findall('Sample'):
    index = sample.find('Index').text
    description_element = sample.find('Description')
    description = description_element.text if description_element is not None and description_element.text is not None else 'Empty'

    python_code_element = sample.find('PythonCode')
    if python_code_element is not None:
        python_code = python_code_element.text

    try:
        # load python files
        with open(f'resources/pythoncodes/{index}_generated_sim.py', 'r') as file:
            content = file.read()
            if python_code is None:
                python_code = content
    except FileNotFoundError:
        print(f"Error: The file '{index}' was not found.")

    # Create a dictionary for each sample
    sample_dict = {
        'Index': index,
        'Description': description,
        'PythonCode': python_code
    }

    # Append the dictionary to the dataset list
    dataset.append(sample_dict)
    DESCRIPTIONS.append(description)  # For BM25

print(f'Loaded {len(dataset)} entries')


# === CREATE BM25 INDEX ===
tokenized_descriptions = [desc.lower().split() for desc in DESCRIPTIONS]
bm25 = BM25Okapi(tokenized_descriptions)


def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk, options={'num-ctx': 4096})['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))


for i, chunk in enumerate(dataset):
    desc =chunk['Description']
    print (len(desc))
    add_chunk_to_database(desc)
    print(f'Added chunk {i + 1}/{len(dataset)} to the database')


def cosine_similarity(a, b):
    dot_product = sum([x * y for x, y in zip(a, b)])
    norm_a = sum([x ** 2 for x in a]) ** 0.5
    norm_b = sum([x ** 2 for x in b]) ** 0.5
    return dot_product / (norm_a * norm_b)


def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    # temporary list to store (chunk, similarity) pairs
    similarities = []
    index = 1
    for chunk, embedding in VECTOR_DB:
        similarity = cosine_similarity(query_embedding, embedding)
        similarities.append((index, chunk, similarity))
    # sort by similarity in descending order, because higher similarity means more relevant chunks
    similarities.sort(key=lambda x: x[2], reverse=True)
    # finally, return the top N most relevant chunks
    return similarities[:top_n]


# input_query = input('Ask me a question: ')
# retrieved_knowledge = retrieve(input_query)
#
# details = []
# print('Retrieved knowledge:')
# for index, chunk, similarity in retrieved_knowledge:
#     print(f' - (similarity: {similarity:.2f}) {chunk}')
#     details.append({'Description': chunk,
#                     'PythonCode': dataset[index-1]['PythonCode']})
#
# instruction_prompt = f'''You are a helpful chatbot.
# Use only the following pieces of context to answer the question. Don't make up any new information:
# {'\n'.join([f' - {chunk}' for index, chunk, similarity in retrieved_knowledge])}
# '''
#
# stream = ollama.chat(
#     model=LANGUAGE_MODEL,
#     messages=[
#         {'role': 'system', 'content': instruction_prompt},
#         {'role': 'user', 'content': input_query},
#     ],
#     stream=True,
# )
#
# # print the response from the chatbot in real-time
# print('Chatbot response:')
# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)
