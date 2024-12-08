import fitz  
file_path = r"C:\Users\sarve\OneDrive\Desktop\sar\188.pdf"  


pdf_document = fitz.open(file_path)

old_text = "5.3.3 / 2023-2024/ DT Row No  189"
new_text = "5.3.3 / 2023-2024/ DT Row No  188"


for page_num, page in enumerate(pdf_document, start=1):
    text_instances = page.search_for(old_text)  
    if text_instances:  
        for inst in text_instances:
           
            x0, y0, x1, y1 = inst
            
            page.add_redact_annot(inst)
        
        
        page.apply_redactions()

        
        for inst in text_instances:
            x0, y0, x1, y1 = inst
            page.insert_text((x0, y0), new_text, fontsize=12, color=(0, 0, 0))


pdf_document.save("row 188.pdf")  
pdf_document.close()

print("Relabeling complete!")
