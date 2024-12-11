import os
import hashlib

def get_file_hash(file_path, hash_algo="md5"):
    """Calculate the hash of a file using the specified algorithm (default: MD5)."""
    hash_func = hashlib.new(hash_algo)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def find_duplicates(directory_path):
    """Detect and print duplicate files in a given directory."""
    file_hashes = {}
    duplicates = []
    
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            
            file_hash = get_file_hash(file_path)
            
            
            if file_hash in file_hashes:
                duplicates.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path
    
    
    if duplicates:
        print("Duplicate files found:")
        for dup in duplicates:
            print(f"Duplicate: {dup[0]} <--> Original: {dup[1]}")
    else:
        print("No duplicates found.")


directory_path = r"C:\Users\sarve\OneDrive\Desktop\all pdf"  
find_duplicates(directory_path)
