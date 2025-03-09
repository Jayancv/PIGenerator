import ollama
import xml.etree.ElementTree as ET

# Load dataset
dataset = []
tree = ET.parse('rag_system/resources/dataset.xml')
root = tree.getroot()

for sample in root.findall('Sample'):
    index = sample.find('Index').text
    description_element = sample.find('Description')
    description = description_element.text if description_element is not None and description_element.text is not None else 'Empty'

    python_code_element = sample.find('PythonCode')
    python_code = python_code_element.text if python_code_element is not None else None

    try:
        # Load Python files
        with open(f'resources/pythoncodes/{index}_generated_sim.py', 'r') as file:
            content = file.read()
            if python_code is None:
                python_code = content
    except FileNotFoundError:
        print(f"Error: The file '{index}' was not found.")

    dataset.append({'Index': index, 'Description': description, 'PythonCode': python_code})

print(f'Loaded {len(dataset)} entries')

# Embedding and language models
EMBEDDING_MODEL = 'nomic-embed-text'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'
VECTOR_DB = []

# Function to add chunks to the database
def add_chunk_to_database(chunk):
    embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
    VECTOR_DB.append((chunk, embedding))

# Populate vector database
for i, chunk in enumerate(dataset):
    add_chunk_to_database(chunk['Description'])
    print(f'Added chunk {i + 1}/{len(dataset)} to the database')

print(f"Total {len(VECTOR_DB)} descriptions embedded.")
print("✅ Vector Database is ready for retrieval!")

# Cosine similarity function
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x ** 2 for x in a) ** 0.5
    norm_b = sum(x ** 2 for x in b) ** 0.5
    return dot_product / (norm_a * norm_b)

# Retrieve relevant details
def retrieve(query, top_n=3):
    query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
    similarities = [(index, chunk, cosine_similarity(query_embedding, embedding)) for index, (chunk, embedding) in enumerate(VECTOR_DB)]
    similarities.sort(key=lambda x: x[2], reverse=True)
    return similarities[:top_n]

# Function to fetch details based on a query
def get_retrieved_details(query):
    retrieved_knowledge = retrieve(query)
    details = [{'Description': chunk, 'PythonCode': dataset[index]['PythonCode']} for index, chunk, _ in retrieved_knowledge]
    return details
