import chromadb
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings, VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import os, time, openai, inquirer

def prompt_user():
  questions = [
    inquirer.Text('query', message="Ask me anything")
  ]
  answers = inquirer.prompt(questions)
  return answers['query']

openai.api_key = os.getenv("OPENAI_API_KEY")

tic = time.perf_counter()
# load some documents
documents = SimpleDirectoryReader("./data").load_data()
toc = time.perf_counter()

print(f"Loaded documents in {toc - tic:0.4f} seconds")

tic = time.perf_counter()
# initialize client
db = chromadb.PersistentClient(path="./chroma_db")

# get collection
chroma_collection = db.get_or_create_collection("ca-payphone")

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
toc = time.perf_counter()

print(f"Chroma DB loaded in {toc - tic:0.4f} seconds")

tic = time.perf_counter()
# create your index
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)
toc = time.perf_counter()

print(f"Index created in {toc - tic:0.4f} seconds")

Settings.llm = OpenAI(
  model="gpt-4o-mini", 
)

# create a query engine and query
query_engine = index.as_query_engine()

while True: 
  user_query = prompt_user()

  #Allow for graceful exit
  if user_query.lower() in ['exit', 'quit']:
      break

  tic = time.perf_counter()
  response = query_engine.query(user_query)
  toc = time.perf_counter()
  print(f"Open AI query completed in {toc - tic:0.4f} seconds")
  print(response)

