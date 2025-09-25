# Langchain-Tutorial-paid-and-open-source-
Simple chatbot implementation using LangChain, with both OpenAI’s paid API and the free open-source Ollama model.


# Setup Local Development with Ollama

This guide explains how to set up your local environment using **VS Code** and **Ollama**.

---

## 1. Install Ollama

Download and install Ollama from the official website:

👉 [https://ollama.ai/download](https://ollama.ai/download)

---

## 2. Verify Installation

Open a terminal and run:

```bash
ollama --version
```

---

## 3. Run an Ollama Model

You can pull and run models locally, for example llama3:
```
ollama pull llama3
ollama run llama3
```

---

## 4. Clone the Repository

Clone your GitHub repo to your local machine:
```
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```
---

## 5. Open with VS Code

Launch VS Code in the repo folder:
```
code .
```
---

## 6. Setup Python Environment

Make sure you have Python 3.9+ installed. Create a virtual environment:

```
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```
---

## Install dependencies:
```
pip install -r requirements.txt
```
---

## 7. Connect Your Code with Ollama

In your Python/JS code, you can call Ollama locally.
Example (Python):
```
from ollama import Client

client = Client()
response = client.chat(model="llama3", messages=[{"role": "user", "content": "Hello Ollama!"}])
print(response["message"]["content"])
```

### ✅ Now you are ready to run and test your project locally with Ollama + VS Code!
