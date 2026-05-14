import os
import random
import string
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFGenerator:
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        self._prepare_directory()

    def _prepare_directory(self):
        """Ensures the output directory is clean and ready."""
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir)

    @staticmethod
    def generate_dummy_text(keywords, length=800):
        """Generates a pseudo-random text based on provided keywords."""
        base_vocabulary = ["framework", "infrastructure", "paradigm", "scalability", "integration"]
        word_pool = base_vocabulary + keywords

        words = [
            random.choice(word_pool) + "".join(random.choices(string.ascii_lowercase, k=2))
            for _ in range(length)
        ]
        return " ".join(words)

    def create_pdf(self, file_name, title, keywords):
        """Generates a professional-looking PDF document."""
        file_path = os.path.join(self.output_dir, file_name)
        try:
            c = canvas.Canvas(file_path, pagesize=letter)

            # Header
            c.setFont("Helvetica-Bold", 18)
            c.drawString(72, 730, title)
            c.setStrokeColorRGB(0.2, 0.2, 0.2)
            c.line(72, 720, 540, 720)

            # Content
            c.setFont("Helvetica", 10)
            text_object = c.beginText(72, 690)
            text_object.setLeading(14)

            raw_text = self.generate_dummy_text(keywords)
            # Wrap text manually
            lines = [raw_text[i:i + 90] for i in range(0, len(raw_text), 90)]

            for line in lines:
                text_object.textLine(line)
                if text_object.getY() < 50:
                    c.drawText(text_object)
                    c.showPage()
                    text_object = c.beginText(72, 750)
                    text_object.setFont("Helvetica", 10)

            c.drawText(text_object)
            c.save()
            return True
        except Exception as e:
            print(f"[!] Error creating {file_name}: {e}")
            return False