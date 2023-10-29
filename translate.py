

import streamlit as st
from PyPDF2 import PdfReader, PdfMerger
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from googletrans import Translator, LANGUAGES as googletrans_languages
from langchain.callbacks import get_openai_callback
import pickle
import os
import base64
from dotenv import load_dotenv
# Background images add function
# (your add_bg_from_local function remains unchanged)
load_dotenv()
# def main():
#     st.header("📄🤗")

    # # Upload multiple PDF files
    # pdf_files = st.file_uploader("Upload your Multiple PDF files", type='pdf', accept_multiple_files=True)

    # # Initialize query outside the loop
    # query = ""

    # if pdf_files:
    #     merged_pdf_name = "merged.pdf"
    #     merger = PdfMerger()

    #     for pdf in pdf_files:
    #         # Extract text from each PDF
    #         pdf_reader = PdfReader(pdf)
    #         text = ""
    #         for page in pdf_reader.pages:
    #             text += page.extract_text()

    #         # Langchain text splitter
    #         text_splitter = RecursiveCharacterTextSplitter(
    #             chunk_size=1000,
    #             chunk_overlap=200,
    #             length_function=len
    #         )

    #         chunks = text_splitter.split_text(text=text)

    #         # Store PDF name
    #         store_name = pdf.name[:-4]

    #         if os.path.exists(f"{store_name}.pkl"):
    #             with open(f"{store_name}.pkl", "rb") as f:
    #                 vectorstore = pickle.load(f)
    #         else:
    #             # Embeddings (OpenAI methods)
    #             embeddings = OpenAIEmbeddings(openai_api_key="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")

    #             # Store the chunks part in the database (vector)
    #             vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

    #             with open(f"{store_name}.pkl", "wb") as f:
    #                 pickle.dump(vectorstore, f)

    #         # Merge the PDFs
    #         merger.append(pdf)

    #     if merger.pages:
    #         merger.write(merged_pdf_name)
    #         merger.close()

    #         # Accept user questions/query
    #         query = st.text_input("Ask questions about related your upload PDF file")

    #         if query:
    #             docs = vectorstore.similarity_search(query=query, k=3)

    #             # OpenAI rank LNV process
    #             llm = OpenAI(temperature=0)
    #             chain = load_qa_chain(llm=llm, chain_type="stuff")

    #             with st.form("language_selection"):
    #                 st.write("Select language for the answer:")
    #                 # Allow users to select any destination language
    #                 dest_lang = st.selectbox("Select destination language:",
    #                                         list(googletrans_languages.values()))
    #                 submit_button = st.form_submit_button(
    #                     "Translate and Display Answer")

    #             if submit_button:
    #                 with get_openai_callback() as cb:
    #                     response = chain.run(input_documents=docs, question=query)
    #                     st.write("PDF Chatbot Response:")
    #                     st.write(response)

    #                 try:
    #                     translator = Translator()
    #                     translation = translator.translate(
    #                         response, src="en", dest=dest_lang)
    #                     if translation is not None and hasattr(translation, 'text') and translation.text:
    #                         st.write(
    #                             f"**Translated Answer ({dest_lang}):** {translation.text}")
    #                     else:
    #                         st.error(
    #                             "Translation failed. Please check your input and try again.")
    #                 except Exception as e:
    #                     st.error(f"An error occurred during translation: {str(e)}")



# if __name__ == "__main__":
#     main()





# # C:\Users\deepgohil\Desktop\datahack linkedin\PDFBasedChatBot_With_Translator_Using_Streamlit\pdfchatbot_streamlit\translate.py



# Streamlit library, used to create the user interface for the application.
import streamlit as st
# Module from the Langchain library that provides embeddings for text processing using OpenAI language models.
from langchain.embeddings.openai import OpenAIEmbeddings
# Python built-in module for handling temporary files.
import tempfile
# Python built-in module for time-related operations.
import time
# Below are the classes from the Langchain library
from langchain import OpenAI, PromptTemplate, LLMChain
# class from the Langchain library that splits text into smaller chunks based on specified parameters.
from langchain.text_splitter import CharacterTextSplitter
# This is a class from the Langchain library that loads PDF documents and splits them into pages.
from langchain.document_loaders import PyPDFLoader
# This is a function from the Langchain library that loads a summarization chain for generating summaries.
from langchain.chains.summarize import load_summarize_chain
# This is a class from the Langchain library that represents a document.
from langchain.docstore.document import Document
# This is a class from the Langchain library that provides vector indexing and similarity search using FAISS.
from langchain.vectorstores import FAISS
# This is a function from the Langchain library that loads a question-answering chain for generating answers to questions.
from langchain.chains.question_answering import load_qa_chain





import streamlit as st
import os

# ... (your imports and other code remain unchanged) ...

def main():
    st.sidebar.header("Options")

    # Add options to the sidebar
    selected_option = st.sidebar.selectbox("Select an Option", ["Search in your PDF", "PDF summeriztion", "PDF Translation"])

    if selected_option == "Search in your PDF":
        st.header("📄🤗")
    # Upload multiple PDF files
    pdf_files = st.file_uploader("Upload your Multiple PDF files", type='pdf', accept_multiple_files=True)

    # Initialize query outside the loop
    query = ""

    if pdf_files:
        merged_pdf_name = "merged.pdf"
        merger = PdfMerger()

        for pdf in pdf_files:
            # Extract text from each PDF
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Langchain text splitter
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )

            chunks = text_splitter.split_text(text=text)

            # Store PDF name
            store_name = pdf.name[:-4]

            if os.path.exists(f"{store_name}.pkl"):
                with open(f"{store_name}.pkl", "rb") as f:
                    vectorstore = pickle.load(f)
            else:
                # Embeddings (OpenAI methods)
                embeddings = OpenAIEmbeddings(openai_api_key="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")

                # Store the chunks part in the database (vector)
                vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

                with open(f"{store_name}.pkl", "wb") as f:
                    pickle.dump(vectorstore, f)

            # Merge the PDFs
            merger.append(pdf)

        if merger.pages:
            merger.write(merged_pdf_name)
            merger.close()

            # Accept user questions/query
            query = st.text_input("Ask questions about related your upload PDF file")

            if query:
                docs = vectorstore.similarity_search(query=query, k=3)

                # OpenAI rank LNV process
                llm = OpenAI(temperature=0)
                chain = load_qa_chain(llm=llm, chain_type="stuff")

                with st.form("language_selection"):
                    st.write("Select language for the answer:")
                    # Allow users to select any destination language
                    dest_lang = st.selectbox("Select destination language:",
                                            list(googletrans_languages.values()))
                    submit_button = st.form_submit_button(
                        "Translate and Display Answer")

                if submit_button:
                    with get_openai_callback() as cb:
                        response = chain.run(input_documents=docs, question=query)
                        st.write("PDF Chatbot Response:")
                        st.write(response)

                    try:
                        translator = Translator()
                        translation = translator.translate(
                            response, src="en", dest=dest_lang)
                        if translation is not None and hasattr(translation, 'text') and translation.text:
                            st.write(
                                f"**Translated Answer ({dest_lang}):** {translation.text}")
                        else:
                            st.error(
                                "Translation failed. Please check your input and try again.")
                    except Exception as e:
                        st.error(f"An error occurred during translation: {str(e)}")

    elif selected_option == "PDF summeriztion":

        llm = OpenAI(openai_api_key="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", temperature=0)

        # We need to split the text using Character Text Split such that it should not increase token size
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=800,
            chunk_overlap=200,
            length_function=len,
        )

        st.title("PDF Summarizer & QA")
        pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

        if pdf_file is not None:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(pdf_file.read())
                pdf_path = tmp_file.name
                loader = PyPDFLoader(pdf_path)
                pages = loader.load_and_split()

                page_selection = st.radio("Page selection", ["Single page", "Page range", "Overall Summary", "Question"])

                if page_selection == "Single page":
                    page_number = st.number_input("Enter page number", min_value=1, max_value=len(pages), value=1, step=1)
                    view = pages[page_number - 1]
                    texts = text_splitter.split_text(view.page_content)
                    docs = [Document(page_content=t) for t in texts]
                    chain = load_summarize_chain(llm, chain_type="map_reduce")
                    summaries = chain.run(docs)

                    st.subheader("Summary")
                    st.write(summaries)

                elif page_selection == "Page range":
                    start_page = st.number_input("Enter start page", min_value=1, max_value=len(pages), value=1, step=1)
                    end_page = st.number_input("Enter end page", min_value=start_page, max_value=len(pages), value=start_page, step=1)

                    texts = []
                    for page_number in range(start_page, end_page + 1):
                        view = pages[page_number - 1]
                        page_texts = text_splitter.split_text(view.page_content)
                        texts.extend(page_texts)
                    docs = [Document(page_content=t) for t in texts]
                    chain = load_summarize_chain(llm, chain_type="map_reduce")
                    summaries = chain.run(docs)
                    st.subheader("Summary")
                    st.write(summaries)

                elif page_selection == "Overall Summary":
                    combined_content = ''.join([p.page_content for p in pages])  # we get entire page data
                    texts = text_splitter.split_text(combined_content)
                    docs = [Document(page_content=t) for t in texts]
                    chain = load_summarize_chain(llm, chain_type="map_reduce")
                    summaries = chain.run(docs)
                    st.subheader("Summary")
                    st.write(summaries)
                elif page_selection == "Question":
                    question = st.text_input("Enter your question", value="Enter your question here...")
                    combined_content = ''.join([p.page_content for p in pages])
                    texts = text_splitter.split_text(combined_content)
                    embedding = OpenAIEmbeddings(openai_api_key='your_openai_api_key')
                    document_search = FAISS.from_texts(texts, embedding)
                    chain = load_qa_chain(llm, chain_type="stuff")
                    docs = document_search.similarity_search(question)
                    summaries = chain.run(input_documents=docs, question=question)
                    st.write(summaries)

        else:
            time.sleep(30)
            st.warning("No PDF file uploaded")    
    elif selected_option == "PDF Translation":
        # Execute test.py when PDF summeriztion is selected
        os.system("python test.py")

if __name__ == "__main__":
    main()
# In this modified version of your code, a sidebar is added using st.sidebar. Two options ("Search in your PDF" and "PDF summeriztion") are provided in the sidebar. When "PDF summeriztion" is selected, os.system("python test.py") is executed, which runs test.py. Please make sure test.py is in the same directory or provide the correct path if it's located elsewhere. You might need to adjust the path accordingly based on your project structure.





