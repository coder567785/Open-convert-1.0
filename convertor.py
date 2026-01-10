import os
from PIL import Image
from reportlab.pdfgen import canvas
import win32com.client

def convert_file(input_path, output_format):
    base, ext = os.path.splitext(input_path)
    ext = ext.lower()
    output_format = output_format.lower()

    # ---------- IMAGE CONVERSIONS ----------
    image_exts = [".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"]

    if ext in image_exts and output_format in ["png", "jpg", "jpeg", "webp", "bmp", "tiff"]:
        img = Image.open(input_path)

        if output_format in ["jpg", "jpeg"]:
            img = img.convert("RGB")

        output_path = base + "." + output_format
        img.save(output_path, output_format.upper())
        return output_path

    # ---------- TXT → PDF ----------
    if ext == ".txt" and output_format == "pdf":
        output_path = base + ".pdf"
        c = canvas.Canvas(output_path)
        text = c.beginText(40, 800)

        with open(input_path, "r", encoding="utf-8") as f:
            for line in f:
                text.textLine(line.rstrip())

        c.drawText(text)
        c.save()
        return output_path

    # ---------- DOCX → PDF ----------
    if ext == ".docx" and output_format == "pdf":
        output_path = base + ".pdf"

        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(input_path)
        doc.SaveAs(output_path, FileFormat=17)  # 17 = PDF
        doc.Close()
        word.Quit()

        return output_path

    # ---------- PPT / PPTX → PDF ----------
    if ext in [".ppt", ".pptx"] and output_format == "pdf":
        output_path = base + ".pdf"

        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        presentation = powerpoint.Presentations.Open(input_path, WithWindow=False)
        presentation.SaveAs(output_path, 32)  # 32 = PDF
        presentation.Close()
        powerpoint.Quit()

        return output_path

    # ---------- INVALID ----------
    raise ValueError("This file type cannot be converted to the selected format.")
