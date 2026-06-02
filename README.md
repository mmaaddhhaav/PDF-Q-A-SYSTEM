📚 Chat with Multiple PDFs using Gemini AI 🚀
AI-powered Q&A system for multiple PDF documents. Upload files, process text, and ask questions in natural language. Uses RAG, FAISS, Hugging Face embeddings, and Google Gemini AI for context-aware answers.

✨ Features:
1).📄 Upload multiple PDFs
2).🔍 Automatic text extraction
3).🧠 Semantic search with embeddings
4).🤖 Gemini-powered answers
5).⚡ Fast retrieval with FAISS
6).🎨 Streamlit web interface

🏗️ Architecture
Code
Upload PDFs → Extract Text → Chunk Text → Generate Embeddings → Store in FAISS → Ask Question → Retrieve Context → Gemini AI → Answer
🛠️ Tech Stack
Frontend: Streamlit
Backend: Python
AI/ML: Gemini AI, Hugging Face
Database: FAISS
Libraries: LangChain, PyPDF2, dotenv

⚙️ Setup
bash
git clone https://github.com/yourusername/pdf-chatbot.git
cd pdf-chatbot
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
Add .env:

Code
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
▶️ Run
bash
streamlit run main.py
👉 App runs at: http://localhost:8501

📖 Usage
1).Upload PDFs
2).Click Process
3).Ask questions

Get contextual answers

🔮 Future
1).DOCX/TXT support
2).Citations & source highlighting
3).Cloud deployment
4).Voice & OCR

👨‍💻 Author
Madhav Sharma  
B.Tech CSE | Passionate about AI, ML, DSA & Full-Stack Development
