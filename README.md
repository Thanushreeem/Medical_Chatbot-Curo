# 🩺 Curo – AI Medical Chatbot

Curo is an AI-powered medical chatbot that answers health-related questions using Large Language Models (LLMs) and medical knowledge from PDF documents.  
It uses Retrieval-Augmented Generation (RAG) to provide context-aware and reliable responses.

⚠️ Disclaimer: This chatbot is for informational purposes only and not a substitute for professional medical advice.

---

#  Features

✅ Ask health & medical questions  
✅ PDF-based knowledge retrieval (RAG)  
✅ Groq LLM for fast AI responses  
✅ Pinecone vector database for embeddings  
✅ Modern UI with chat interface  
✅ Flask backend  
✅ Responsive design  
✅ Resume-ready AI project

---

#  Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Flask (Python)
- **LLM:** Groq API
- **Embeddings:** HuggingFace sentence-transformers
- **Vector DB:** Pinecone
- **RAG Pipeline:** LangChain
- **Deployment:** Render / Railway / HuggingFace Spaces

---

# Project Structure

Medical_Chatbot/
│
├── Data/ # Medical PDFs
├── src/
│ ├── helper.py # Embeddings & loader functions
│ ├── prompt.py # Prompt templates
│
├── static/
│ ├── style.css
│ ├── bot.png
│
├── templates/
│ ├── chat.html
│
├── app.py # Flask app
├── store_index.py # Pinecone indexing
├── requirements.txt
├── .env
└── README.md

# Add Environment Variables
Create .env file:
    GROQ_API_KEY=your_key
    PINECONE_API_KEY=your_key

# How to run the project 
# Create & Activate Conda Environment
1️⃣ Create environment
    conda create -n your_Environment_name python=3.10
2️⃣ Activate environment
    conda activate your_Environment_name


# Install Dependencies
pip install -r requirements.txt

# Store Embeddings in Pinecone 
python store_index.py(only once you have to run)

# Run App
python app.py