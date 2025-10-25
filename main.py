from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os 
import pandas as pd
from langchain_community.document_loaders import UnstructuredPDFLoader


doc_path = './data/introducaoProgramacao.pdf'
model = 'gemma3'

# ==== Ingestão de PDF ====

if doc_path:
    loader = UnstructuredPDFLoader(file_path=doc_path, languages=['por'])
    data = loader.load()
    print("Leitura concluida")
else:
    print("Falha na leitura, arquivo não encontrado!")

# preview da primeira pagina:
content = data[0].page_content
#print(content[:100])

# ==== Extrai texto do PDF e divide em pedaços pequenos (Small Chunks) ====

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("divisão em chunks completa...")

# ==== Adiciona para a database de vetores ====

import ollama
ollama.pull('nomic-embed-text')

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model='nomic-embed-text'),
    collection_name='simple-rag'
)

print("Adição ao database de vetores concluida...")

# ==== Retrieval ====
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain_core.runnables import RunnablePassthrough
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

llm = ChatOllama(model=model)

QUERY_PROMPT = PromptTemplate(
    input_variables=['question'],
    template="""Você é um monitor da cadeira de introdução a programação.
    Sua função é responder perguntas sobre essa cadeira tendo todas as 
    respostas embasadas no material fornecido no vector database.
    
    Responda a pergunta: {question}"""
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)

template = """Responda a pergunta se baseando APENAS E SOMENTE no 
contexto fonecido a seguir: {contexto}
Pergunta: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {'contexto': retriever, 'question': RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("Chat iniciado, digite suas perguntas!")
while True:
    pergunta = input(">>")
    
    if pergunta == 'q':
        break

    res = chain.invoke(input=(pergunta,))
    print(res)