from pathlib import Path
from PyPDF2 import PdfReader

class FileText:
    def __init__(self, file_path):
        script_dir = Path(__file__).parent
        #self.file_path = Path(file_path).resolve()
        self.file_path = script_dir / file_path
        self.file_extention = self.file_path.suffix

    def get_text_from_txt(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        return file_content

    def get_text_from_pdf(self):
        # Open your PDF file
        with open(self.file_path, "rb") as file:
            reader = PdfReader(file)
            text = ""

            # Loop through all pages
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text

    def get_text(self):
        file_path = self.file_path
        file_extention = file_path.suffix

        file_text = ""
        if "pdf" in file_extention.lower():
            file_text = self.get_text_from_pdf()
        elif "txt" in file_extention.lower():
            file_text = self.get_text_from_txt()

        return file_text