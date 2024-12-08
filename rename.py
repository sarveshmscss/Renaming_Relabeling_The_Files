import os


directory = r"C:\Users\sarve\OneDrive\Desktop\sar"


for filename in sorted(os.listdir(directory), reverse=True):
    if filename.startswith("row ") and filename[4:].split('.')[0].isdigit():
        
        row_number = int(filename[4:].split('.')[0])
        file_extension = os.path.splitext(filename)[1] 

        
        if 184 <= row_number <= 244:
            new_row_number = row_number - 1  
            new_filename = f"row {new_row_number}{file_extension}"
            temp_filename = f"temp_{new_row_number}{file_extension}"  

           
            old_file_path = os.path.join(directory, filename)
            temp_file_path = os.path.join(directory, temp_filename)

            
            os.rename(old_file_path, temp_file_path)
            print(f"Temporarily renamed: {filename} -> {temp_filename}")


for filename in os.listdir(directory):
    if filename.startswith("temp_"):
        new_filename = filename.replace("temp_", "")
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f"Finalized rename: {filename} -> {new_filename}")

print("File renaming complete!")
