import fitz  # PyMuPDF
import os

folder_path = r"C:\Users\sarve\OneDrive\Desktop\245-305"

start_row = 246
end_row = 306

for i in range(start_row, end_row + 1):
    file_name = f"row {i}.pdf"
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        print(f"Processing file: {file_path}")
        
        pdf_document = fitz.open(file_path)

        # Define old and new text
        old_text = f"5.3.3 / 2023-2024/ DT Row No  {i}"
        new_text = f"5.3.3 / 2023-2024/ DT Row No  {i - 1}"

        for page_num, page in enumerate(pdf_document, start=1):
            # Search for the old text in the page
            text_instances = page.search_for(old_text)
            if text_instances:
                # Apply redactions over the old text
                for inst in text_instances:
                    page.add_redact_annot(inst)

                page.apply_redactions()

                # Insert new text in the same location
                for inst in text_instances:
                    x0, y0, x1, y1 = inst
                    page.insert_text((x0, y0), new_text, fontsize=12, color=(0, 0, 0))

        # Save the updated file
        updated_file_path = os.path.join(folder_path, f"row {i - 1}.pdf")
        pdf_document.save(updated_file_path)
        pdf_document.close()

        print(f"Relabeling complete for {file_path}!")
    else:
        print(f"File {file_path} not found.")

print("All files processed.")
