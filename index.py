# importing required modules
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open('nomina.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
 
# printing number of pages in pdf file
print(len(pdfReader.pages))
 
# creating a page object
pageObj = pdfReader.pages[0]

for page in pdfReader.pages:
    print(page.extract_text())
    
 
# extracting text from page
 
# closing the pdf file object
pdfFileObj.close()