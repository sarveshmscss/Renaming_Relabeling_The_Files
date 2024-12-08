
# 📄 PDF File Processing and Relabeling Script

## 📝 Overview
These scripts automates the process of manipulating and relabeling PDF files in a directory. It performs three main tasks:

### 1. **🔍 Open PDF Files in Microsoft Edge**
The script starts by scanning a specific directory for `.pdf` files. It then opens each of these PDF files in Microsoft Edge for review or inspection.

### 2. **🔄 Relabeling PDFs**
The script includes functionality to search for and replace specific text within the PDF files. Specifically, it searches for a row identifier in the text (e.g., "DT Row No 189") and replaces it with a new row identifier (e.g., "DT Row No 188"). It does this by:
- Searching the text in each PDF page.
- Applying a redaction to remove the old row number.
- Inserting the new row number in its place.

The updated files are saved with a new name that reflects the modified row number.

### 3. **🔧 File Renaming**
After processing the PDF files, the script performs file renaming in the directory. It reduces the row number (e.g., `row 189` becomes `row 188`). The renaming is done in two steps:
- Initially, the file is temporarily renamed.
- Then, the temporary file is renamed to its final name with the updated row number.

---

## 🌟 Features:
- **📂 Batch File Processing**: The script processes multiple PDF files automatically, making it highly efficient for large datasets.
- **🔎 Text Replacement in PDFs**: It offers robust functionality for finding and replacing specific text across multiple pages of a PDF file.
- **📁 File Organization**: It helps keep files organized by renaming them systematically according to the processed row numbers.
- **💻 Edge Browser Integration**: Uses Microsoft Edge to open PDF files for quick viewing or inspection.

---

## 🛠️ Requirements:
- **Python 3.x**.
- **PyMuPDF (fitz)**: For PDF file manipulation. You can install it using:
  ```
  pip install pymupdf
  ```
- **Microsoft Edge**: Must be installed and accessible from the command line as `msedge`.

---

## 🚀 How to Use:

### 1. Clone or download the script to your local machine.

### 2. Install the required dependencies:
```bash
pip install pymupdf
```

### 3. Modify the `folder_path` in the script to the directory where your PDF files are stored.

### 4. Run the script:
```bash
python script_name.py
```

### 5. The script will process the files, relabel them, and rename them accordingly.

---

## 📋 Example:

For a file named `row 189.pdf`, the script will:
1. **Open** it in Microsoft Edge for inspection.
2. **Replace** the text `"DT Row No 189"` with `"DT Row No 188"`.
3. **Rename** the file from `row 189.pdf` to `row 188.pdf`.

---

## 📂 File Organization After Processing:
- **Updated PDF files** with new row numbers.
- **Renamed files** that follow a consistent naming pattern (e.g., `row 188.pdf`, `row 189.pdf`, etc.).
  
