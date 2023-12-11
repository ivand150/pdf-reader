# importing required modules
import PyPDF2

# creating pdf path
pdfIle = 'nomina.pdf'
 
# creating a pdf file object
pdfFileObj = open(pdfIle, 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
 
# printing number of pages in pdf file
print(len(pdfReader.pages))

pageNumber = 1
 
# extracting text from pages
for page in pdfReader.pages:
    print('PAGE: ', pageNumber)
    print(page.extract_text())
    pageNumber += 1
    
# closing the pdf file object
pdfFileObj.close()