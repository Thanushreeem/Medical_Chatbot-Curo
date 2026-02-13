import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

# LangChain
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq

# FIXED IMPORTS ↓
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
from flask import Flask, render_template, request

from dotenv import load_dotenv

# Your files
from src.helper import download_hugging_face_embeddings
from src.prompt import system_prompt

# ===== LOAD ENV =====
load_dotenv()

app = Flask(__name__)

# ===== EMBEDDINGS =====
embeddings = download_hugging_face_embeddings()

# ===== PINECONE INDEX =====
index_name = "chatbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# ✅ GROQ LLM (FREE)

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.4
)




# ===== PROMPT =====
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# ===== RAG CHAIN =====
qa_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, qa_chain)

# ===== ROUTES =====
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]

    try:
        response = rag_chain.invoke({"input": msg})
        return response["answer"]
    except Exception as e:
        print("ERROR:", e)
        return "Error occurred. Check terminal."

# ===== RUN =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
