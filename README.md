📚 Chat with Multiple PDFs using Gemini AI
🚀 Overview

Chat with Multiple PDFs is an AI-powered document question-answering system that allows users to upload multiple PDF files and ask questions in natural language. The application processes the uploaded documents, creates semantic embeddings, and retrieves relevant information to generate accurate answers using Google's Gemini AI.

The project combines Retrieval-Augmented Generation (RAG), Vector Databases, Embeddings, and Large Language Models to provide context-aware responses from PDF documents.

✨ Features
📄 Upload multiple PDF documents simultaneously
🔍 Extract and process PDF text automatically
🧠 Semantic search using vector embeddings
🤖 AI-powered question answering using Gemini
💬 Interactive chatbot interface
📚 Context-aware conversations
⚡ Fast retrieval with FAISS vector database
🎨 Modern Streamlit web interface
🏗️ System Architecture
User Uploads PDFs
        │
        ▼
Text Extraction (PyPDF2)
        │
        ▼
Text Chunking
        │
        ▼
Embeddings Generation
(HuggingFace)
        │
        ▼
FAISS Vector Store
        │
        ▼
User Question
        │
        ▼
Relevant Chunks Retrieval
        │
        ▼
Gemini AI
        │
        ▼
Answer Generation
🛠️ Technologies Used
Frontend
Streamlit
Backend
Python
AI & Machine Learning
Google Gemini AI
Hugging Face Embeddings
Sentence Transformers
Vector Database
FAISS (Facebook AI Similarity Search)
Libraries
LangChain
PyPDF2
Python Dotenv
📂 Project Structure
PDF-Chatbot/
│
├── main.py
├── htmlTemplates.py
├── .env
├── requirements.txt
├── README.md
│
└── assets/
⚙️ Installation
Clone Repository
git clone https://github.com/yourusername/pdf-chatbot.git

cd pdf-chatbot
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

Get your API key from Google AI Studio.

▶️ Running the Application
streamlit run main.py

Application will launch at:

http://localhost:8501
📖 How to Use
Step 1

Upload one or more PDF files.

Step 2

Click the Process button.

Step 3

Wait for embeddings and vector database creation.

Step 4

Ask questions related to the uploaded documents.

Step 5

Receive AI-generated answers with contextual understanding.

🧠 AI Concepts Used
Retrieval-Augmented Generation (RAG)

The project uses RAG architecture to improve answer quality by retrieving relevant document chunks before generating responses.

Vector Embeddings

Text chunks are converted into numerical vectors using Hugging Face Embeddings.

Semantic Search

FAISS performs similarity searches to find the most relevant content for each query.

Conversational Memory

Maintains conversation history for context-aware interactions.

📸 Sample Workflow
Upload PDFs
     ↓
Process Documents
     ↓
Create Embeddings
     ↓
Store in FAISS
     ↓
Ask Questions
     ↓
Retrieve Context
     ↓
Generate Answer using Gemini
🔮 Future Enhancements
Support for DOCX and TXT files
Citation-based answers
Multi-user authentication
Cloud deployment (AWS/Azure/GCP)
Voice-based interaction
OCR support for scanned PDFs
Chat history export
Source highlighting inside PDFs
🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

Retrieval-Augmented Generation (RAG)
LangChain Framework
Vector Databases
Embedding Models
Large Language Models
Prompt Engineering
Streamlit Application Development
AI-powered Search Systems
👨‍💻 Author

Madhav Sharma

B.Tech Computer Science Student

Passionate about Artificial Intelligence, Machine Learning, Data Structures & Algorithms, and Full-Stack Development.
