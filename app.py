import streamlit as st
import pandas as pd
from agents.intake_agent import ElicitationAgent
import docx
import PyPDF2

st.title("WHALE: Multi-Agent Requirements Engineering System")

elicitation_agent = ElicitationAgent()

def extract_requirements(text):
    result = elicitation_agent.process({'content': text, 'format': 'multi'})
    return result.get('sys1_requirements', [])

st.sidebar.header("Upload a requirements document")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "pdf", "docx", "xlsx", "csv"])

st.sidebar.header("Or paste requirements text")
raw_text = st.sidebar.text_area("Paste requirements here")

st.header("Extracted Requirements")

requirements = []

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        requirements = extract_requirements(content)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        content = "\n".join([para.text for para in doc.paragraphs])
        requirements = extract_requirements(content)
    elif uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        requirements = extract_requirements(content)
    elif uploaded_file.type in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text/csv"]:
        df = pd.read_excel(uploaded_file) if uploaded_file.type.endswith("spreadsheetml.sheet") else pd.read_csv(uploaded_file)
        st.write("Uploaded Table:")
        st.dataframe(df)
        # Optionally extract requirements from a column
else:
    if raw_text:
        requirements = extract_requirements(raw_text)

if requirements:
    df = pd.DataFrame(requirements)
    st.dataframe(df)
else:
    st.info("Upload a file or paste requirements text to extract requirements.")

st.markdown("---")
st.write("This is a Streamlit app running on Hugging Face Spaces. Expand it to include review, test generation, and more!") 