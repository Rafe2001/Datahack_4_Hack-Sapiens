# import streamlit as st
# from PyPDF2 import PdfReader
# import openai

# # OpenAI API Key
# openai.api_key = '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'

# # Function to extract text from a PDF file
# def extract_text_from_pdf(uploaded_file):
#     pdf_reader = PdfReader(uploaded_file)
#     text = ''
#     for page_num in range(len(pdf_reader.pages)):
#         text += pdf_reader.pages[page_num].extract_text()
#     return text

# def generate_summary(text):
#     # Split text into chunks of 4096 tokens or less
#     chunks = [text[i:i + 4096] for i in range(0, len(text), 4096)]
    
#     # Generate summary for each chunk and combine them
#     summaries = []
#     for chunk in chunks:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": chunk}
#             ]
#         )
#         if 'choices' in response and len(response.choices) > 0 and 'message' in response.choices[0] and 'content' in response.choices[0].message:
#             summary_chunk = response.choices[0].message['content']
#             summaries.append(summary_chunk)
#         else:
#             st.error("Error generating summary. Please try again.")
    
#     # Combine the summaries
#     summary = ' '.join(summaries)
#     return summary

# # Streamlit UI
# st.title("PDF Summarization App")

# uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

# if uploaded_files:
#     for file in uploaded_files:
#         file_text = extract_text_from_pdf(file)
#         summary = generate_summary(file_text)
#         st.subheader(f"Summary of {file.name}:")
#         st.write(summary)


import streamlit as st 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.chains.summarize import load_summarize_chain
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline
import torch
import base64

#model and tokenizer loading
checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
base_model = T5ForConditionalGeneration.from_pretrained(checkpoint, device_map='auto', torch_dtype=torch.float32)

#file loader and preprocessing
def file_preprocessing(file):
    loader =  PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    final_texts = ""
    for text in texts:
        print(text)
        final_texts = final_texts + text.page_content
    return final_texts

#LLM pipeline
def llm_pipeline(filepath):
    pipe_sum = pipeline(
        'summarization',
        model = base_model,
        tokenizer = tokenizer,
        max_length = 500, 
        min_length = 50)
    input_text = file_preprocessing(filepath)
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result

@st.cache_data
#function to display the PDF of a given file 
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

#streamlit code 
st.set_page_config(layout="wide")

def main():
    st.title("Document Summarization App using Langauge Model")

    uploaded_file = st.file_uploader("Upload your PDF file", type=['pdf'])

    if uploaded_file is not None:
        if st.button("Summarize"):
            col1, col2 = st.columns(2)
            filepath = "data/"+uploaded_file.name
            with open(filepath, "wb") as temp_file:
                temp_file.write(uploaded_file.read())
            with col1:
                st.info("Uploaded File")
                pdf_view = displayPDF(filepath)

            with col2:
                summary = llm_pipeline(filepath)
                st.info("Summarization Complete")
                st.success(summary)


if __name__ == "__main__":
    main()