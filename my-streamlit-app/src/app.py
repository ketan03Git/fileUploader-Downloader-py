import streamlit as st
from utils import save_uploaded_file

def main():
    st.title("File Download App")
    
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "pdf", "jpg", "png"])
    
    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        st.success("File uploaded successfully!")
        
        # Provide a download button
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"Download {uploaded_file.name}",
                data=f,
                file_name=uploaded_file.name
            )

if __name__ == "__main__":
    main()