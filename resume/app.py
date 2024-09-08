import streamlit as st
from PyPDF2 import PdfReader
import pdfplumber
from pyresparser import ResumeParser

def main():
    st.title("Resume Parser")

    uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

        if uploaded_file.type == "application/pdf":
            # Display PDF
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            # Use pdfplumber to display the PDF as images
            with pdfplumber.open("temp.pdf") as pdf:
                for page in pdf.pages:
                    st.image(page.to_image().original, caption=f"Page {page.page_number}")

            # Read the file again for text extraction
            pdf_reader = PdfReader("temp.pdf")
            resume_text = ""
            for page in pdf_reader.pages:
                resume_text += page.extract_text()
        elif uploaded_file.type == "text/plain":
            resume_text = str(uploaded_file.read(), "utf-8")
        else:
            resume_text = "File format not supported yet."

        # Parse the resume using Pyresparser
        parsed_data = ResumeParser("temp.pdf").get_extracted_data()

        st.write("Parsed Information")
        st.json(parsed_data)

        # Extract skills if available
        if 'skills' in parsed_data:
            st.write("Extracted Skills")
            st.json(parsed_data['skills'])

        # Display education and experience if available
        if 'education' in parsed_data:
            st.subheader("Education")
            st.text_area("Education Section", parsed_data['education'], height=200)

        if 'experience' in parsed_data:
            st.subheader("Experience")
            st.text_area("Experience Section", parsed_data['experience'], height=400)

if __name__ == '__main__':
    main()
