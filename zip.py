import zipfile

def create_zip_with_metadata(file_name, comment):
    with zipfile.ZipFile(file_name, 'w') as zipf:
        zipf.writestr("example.txt", "Hello Students Welcome to the Classroom")
        zipf.comment = bytes(comment, 'utf-8')
    print(f"ZIP file created with metadata: {comment}")

# Usage
create_zip_with_metadata("example.zip", "Created by User A on 2024-11-27")
