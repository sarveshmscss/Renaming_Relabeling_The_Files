import os
import subprocess


folder_path = r"C:\Users\sarve\OneDrive\Desktop\85-119"

files = os.listdir(folder_path)


pdf_files = [file for file in files if file.endswith(".pdf")]

for pdf_file in pdf_files:
    file_path = os.path.join(folder_path, pdf_file)
    try:
        
        subprocess.run(["start", "msedge", file_path], shell=True)
        print(f"Opening file: {file_path}")
    except Exception as e:
        print(f"Failed to open file {file_path}: {e}")

print("All files processed.")
