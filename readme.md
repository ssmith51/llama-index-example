# Demo of Llama Index using OpenAI gpt-4o mini
This is an example on how to embed documents (The Iliad) in Chroma DB running locally, and query OpenAI's LLMs. 

This is an example only, it is not for use in production, or a pay phone.

## Installing
1. Execute `pip install -r requirements.txt`
2. Set your OpenAI API Key as an environment variable: `export OPENAI_API_KEY=<your-openai-api-key>`
3. Run the application `python main.py`

## Exting the program
You can exit the program by typing `exit` or `quit`

## Data Stores
Data store access is experimentional. Currently testing: 
- CSV Stores
- Simple Documents (i.e., text files) 

## TODO 
- Add conversation history 
- Determine best way to host a web front end
- Add additionally data store types with proper embedding
- Load index (vector store) w/o reloading on each startup