from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

str1 = "2021.acl-long."
spdf = ".pdf"
stext = ".txt"

number_of_files = 10

# outputFile = open('2021.acl-long.1.txt', 'a')
for i in range(1, int(number_of_files)+1):
    output_string = StringIO()
    with open(str1 + str(i) + spdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    with open(str1 + str(i) + stext, 'w', encoding='utf8') as outputFile:
        outputFile.write(output_string.getvalue())
