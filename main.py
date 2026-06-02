import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI

from htmlTemplates import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""

    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    return text_splitter.split_text(text)


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )

    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain


def handle_user_input(user_question):
    response = st.session_state.conversation_chain(
        {"question": user_question}
    )

    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(st.session_state.chat_history):

        if i % 2 == 0:
            st.write(
                user_template.replace(
                    "{{MSG}}",
                    message.content
                ),
                unsafe_allow_html=True
            )

        else:
            st.write(
                bot_template.replace(
                    "{{MSG}}",
                    message.content
                ),
                unsafe_allow_html=True
            )


def main():

    load_dotenv()

    st.set_page_config(
        page_title="Chat with Multiple PDFs",
        page_icon="📚"
    )

    st.write(css, unsafe_allow_html=True)

    st.header("📚 Chat with Multiple PDFs")

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    user_question = st.text_input(
        "Ask a question about your PDFs:"
    )

    if user_question:

        if st.session_state.conversation_chain is None:

            st.warning(
                "Please upload and process PDFs first."
            )

        else:

            handle_user_input(user_question)

    with st.sidebar:

        st.subheader("Your Documents")

        pdf_docs = st.file_uploader(
            "Upload PDF files",
            accept_multiple_files=True,
            type="pdf"
        )

        if st.button("Process"):

            if not pdf_docs:

                st.warning(
                    "Please upload at least one PDF."
                )

            else:

                with st.spinner("Processing PDFs..."):

                    raw_text = get_pdf_text(pdf_docs)

                    text_chunks = get_text_chunks(raw_text)

                    vectorstore = get_vectorstore(text_chunks)

                    st.session_state.conversation_chain = (
                        get_conversation_chain(vectorstore)
                    )

                    st.success(
                        "✅ PDFs processed successfully!"
                    )


if __name__ == "__main__":
    main()
