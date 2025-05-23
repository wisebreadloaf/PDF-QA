# PDF-QA
---

# 🦜🔗 QA Chatbot Application

This is a simple and interactive Streamlit web application that allows users to upload a PDF and ask detailed questions about its content. The app uses LangChain for document processing and retrieval, OpenAI for embeddings, and Groq's LLaMA 3 model for natural language understanding.

---

## Features

* Upload any PDF document
* Chunk and embed text using OpenAI embeddings
* Store and retrieve data using Chroma vector database
* Ask questions and get detailed answers from the PDF content
* Answers are formatted in markdown for readability

---

## Requirements

* Python 3.8+
* Streamlit
* LangChain
* OpenAI SDK
* Groq SDK
* Chroma
* PyMuPDF (used internally by `PyPDFLoader`)

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-qa-chatbot.git
cd pdf-qa-chatbot
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, you can generate one with:

```bash
pip freeze > requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory or export variables in your terminal:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

Alternatively, in the shell:

```bash
export OPENAI_API_KEY=your_openai_api_key
export GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
.
├── app.py               # Main application script
├── data/                # Stores uploaded PDF files
├── chroma_db/           # Persistent vector store
├── requirements.txt     # Python dependencies
└── README.md            # This readme file
```

---
