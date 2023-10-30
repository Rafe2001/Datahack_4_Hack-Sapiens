import streamlit as st
import os
from llama_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper, SimpleDirectoryReader, ServiceContext
from langchain import OpenAI
import fitz  # PyMuPDF

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to convert uploaded PDF to text and store it in the "text output" directory
def convert_and_store_pdf(pdf_file, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    with open(pdf_file, "rb") as pdf_data:
        pdf = pdf_data.read()
    
    text = extract_text_from_pdf(pdf_file)
    
    text_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".txt"
    text_filepath = os.path.join(output_directory, text_filename)
    
    with open(text_filepath, "w", encoding="utf-8") as text_file:
        text_file.write(text)
    
    return text_filename

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 2000
    max_chunk_overlap = 20
    chunk_size_limit = 500

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, 
                                            model_name="text-davinci-003", 
                                            max_tokens=num_outputs))

    # List of text files created from uploaded PDFs
    pdf_text_files = []

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                text_filename = convert_and_store_pdf(pdf_path, "text output")
                pdf_text_files.append(os.path.join("text output", text_filename))

    documents = SimpleDirectoryReader("text output").load_data()

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    index.save_to_disk('index2.json')

    # Clean up the created text files
    for text_file in pdf_text_files:
        os.remove(text_file)

    return index

def main():
    st.title("Chatbot")
    st.header("This is chatbot answering your Queries")
    os.environ['OPENAI_API_KEY'] = "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"

    uploaded_pdfs = st.file_uploader("Upload multiple PDF files", type=["pdf"], accept_multiple_files=True)
    if uploaded_pdfs:
        with st.spinner("Processing and Storing PDFs..."):
            for uploaded_pdf in uploaded_pdfs:
                temp_dir = "temp_pdf_upload"
                if not os.path.exists(temp_dir):
                    os.makedirs(temp_dir)
                
                pdf_path = os.path.join(temp_dir, uploaded_pdf.name)
                with open(pdf_path, "wb") as pdf_file:
                    pdf_file.write(uploaded_pdf.read())

                # Convert and store each uploaded PDF as text
                text_filename = convert_and_store_pdf(pdf_path, "text output")

                st.success(f"PDF '{uploaded_pdf.name}' converted and stored as '{text_filename}' in the 'text output' directory.")

    if st.button("Construct Index"):
        with st.spinner("Constructing Index..."):
            construct_index('data')
            st.success("Index constructed successfully!")

    query = st.text_input("Ask a question:")
    if st.button("Ask AI"):
        index = GPTSimpleVectorIndex.load_from_disk('index2.json')
        response = index.query(query)
        st.markdown(f"Response: {response.response}")

if __name__ == "__main__":
    main()
