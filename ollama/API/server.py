from fastapi import FastAPI
from langserve import add_routes
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
app=FastAPI(
    title="Essay & Poem Generator API",
    version="1.0",
    description="Generate essays and poems using Ollama LLM")

llm=ChatOllama(
    model='llama3.2:1b'
)

prompt1 = ChatPromptTemplate.from_template('write an essay on {topic} in 100 words')
prompt2 = ChatPromptTemplate.from_template('write an poem on {topic} in 100 words')

add_routes(
    app,
    prompt1|llm,
    path='/essay'
)
add_routes(
    app,
    prompt2|llm,
    path='/poem'
)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8080)