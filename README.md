# 🚀 OpenConvert

A modern, fast, and open-source file converter built with Python & PyQt.  
Convert images, text files, Word documents, and PowerPoint presentations into multiple formats with a clean UI.

> “Simple to use. Powerful under the hood.”

---

## ✨ Features

### 🖼 Image Conversions
Supports:
- Input: `PNG`, `JPG`, `JPEG`, `WEBP`, `BMP`, `TIFF`
- Output: `PNG`, `JPG`, `JPEG`, `WEBP`, `BMP`, `TIFF`

Automatically handles:
- Transparency
- Color conversion (for JPG/JPEG)

---

### 📄 Document Conversions
- `TXT → PDF`
- `DOCX → PDF`
- `PPT → PDF`
- `PPTX → PDF`

(Word & PowerPoint conversions require Microsoft Office to be installed on Windows.)

---

### 🎨 UI
- Built with **PyQt6**
- Dark modern theme
- Simple, minimal workflow:
  1. Select file  
  2. Choose output format  
  3. Click Convert  

Output file is saved in the **same folder** as the input.

---

## 🛠 Tech Stack

- Python 3.10+
- PyQt6 (GUI)
- Pillow (image processing)
- ReportLab (TXT → PDF)
- comtypes (DOCX/PPT → PDF using Windows Office)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/OpenConvert.git
cd OpenConvert

