def save_uploaded_file(uploaded_file):
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return uploaded_file.name

def generate_download_link(file_path):
    return f'<a href="data:file/octet-stream;base64,{file_path}" download>Download {file_path}</a>'