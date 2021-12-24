import os
from io import StringIO
import nltk
from nltk.tokenize import sent_tokenize
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

pdf_folder = "pdf"
text_folder = "pdf2txt"
# check if folder exists if not create it
if not os.path.exists(text_folder):
    os.makedirs(text_folder)

for filename in os.listdir(pdf_folder):
    output_string = StringIO()
    if filename[-4:]!=".pdf":# only process pdf files
      continue
    file_path = os.path.join(pdf_folder, filename)
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    # preprocessing the text
    text = output_string.getvalue()
    text = text.lower()
    text = text.replace("\n\n", ".\n")
    # split into sentences
    sentences = nltk.sent_tokenize(text)
    # remove special characters
    escapes = ''.join([chr(char) for char in range(1, 32)])
    translator = str.maketrans('', '', escapes)
    sentences = [s.translate(translator) for s in sentences]
    # write the text to a file
    textfilename = filename[:-4]+".txt"
    with open(os.path.join(text_folder,textfilename), 'w', encoding='utf8') as outputFile:
        outputFile.write("\n".join(sentences))
