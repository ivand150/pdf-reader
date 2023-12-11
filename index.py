"""Module providing a function printing pdf file"""
import PyPDF2

# creating pdf path
PDF_PATH = 'nomina.pdf'

# creating a pdf file object
pdfFileObj = open(PDF_PATH, 'rb')

# creating a pdf reader objectW
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))

PAGE_NUMBER = 1

# extracting text from pages
for page in pdfReader.pages:
    print('PAGE: ', PAGE_NUMBER)
    print(page.extract_text())
    PAGE_NUMBER += 1

# closing the pdf file object
pdfFileObj.close()
