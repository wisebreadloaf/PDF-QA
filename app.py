import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from groq import Groq

st.title("🦜🔗 QA Chatbot Application")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHROMA_PATH = "./chroma_db"

client = Groq(api_key=GROQ_API_KEY)

if uploaded_file is not None:
    file_path = os.path.join("data", uploaded_file.name)
    os.makedirs("data", exist_ok=True)
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = PyPDFLoader(file_path)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(pages)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=CHROMA_PATH)
    retriever = db.as_retriever()

    st.success("PDF processed and vector store created!")

    def generate_response(query):
        docs = retriever.get_relevant_documents(query)
        context = "\n\n".join([doc.page_content for doc in docs[:3]])

        full_prompt = f"Answer the question based on the following context, answer the questions in a very detailed manner and use markdown for formatting:\n\n{context}\n\nQuestion: {query}"

        chat_completion = client.chat.completions.create(
            model="llama-3-70b-8192",
            messages=[{"role": "user", "content": full_prompt}]
        )
        return chat_completion.choices[0].message.content

    with st.form("query_form"):
        user_query = st.text_area("Ask a question about the PDF:")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner("Generating response..."):
                response = generate_response(user_query)
                st.info(response)
