from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 




# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user","Question: {question}")
    ]
)


## Stremalit framework

st.title("Langchain Demo with OLLAMA llama3")
input_text = st.text_input("Search the topic you want")



## Ollama LLAma3 LLM 
llm = Ollama(model = "llama3")
output_parsers = StrOutputParser()
chain = prompt|llm|output_parsers



if input_text:
    st.write(chain.invoke({"question":input_text}))