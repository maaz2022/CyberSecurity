import zipfile

def read_zip_metadata(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        print(f"ZIP Comment: {zipf.comment.decode()}")
        for info in zipf.infolist():
            print(f"File: {info.filename}, Size: {info.file_size} bytes")

# Usage
read_zip_metadata("example.zip")
