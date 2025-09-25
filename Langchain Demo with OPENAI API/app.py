from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromopTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlir as st
import os 
from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# Langsmith tracking
os.environ["LANFCHAIN_TRACING_V2"] ="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") # helps us to know where the entire monitoring results need to be stored 

# prompt template

prompt = ChatPromopTemplate.from messages(
    "[
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user","Question: {question}")
    ]
)

## Stremalit framework

st.title("Langchain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")


## OPENAI llm
llm = ChatOpenAI(model = "gpt-3.5-turbo")
output_parsers = StrOutputParser()
chain = prompt|llm|output_parsers


if input_text:
    st.write(chain.invoke({"question":input_text}))