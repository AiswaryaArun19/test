import streamlit as st
import requests

# Set up Streamlit app title and description
st.set_page_config(page_title="Gemini API Integration", page_icon=":gem:")
st.title("Gemini API Integration")
st.write("Upload your PDF files to extract text and analyze with the Gemini API.")

# File uploader
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    # Extract text from PDF files
    pdf_text = ""
    for file in uploaded_files:
        pdf_text += "\n" + file.getvalue().decode("utf-8")

    # Gemini API key
    gemini_api_key = st.text_input("Enter your Gemini API key", type="password")

    if gemini_api_key:
        # Gemini API request
        url = "https://gemini-api.example.com/analyze"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {gemini_api_key}"
        }
        data = {
            "text": pdf_text,
            "prompt": "Find the most recurring questions or keywords"
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an exception for non-2xx status codes

            # Display Gemini API results
            st.write("Gemini API Results:")
            st.write(response.json()["results"])

        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")

else:
    st.warning("No files uploaded yet.")