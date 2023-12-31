"""Module providing a function printing pdf file"""
import PyPDF2
import xlsxwriter

# creating pdf path
PDF_PATH = 'nomina.pdf'

# creating a pdf file object
pdfFileObj = open(PDF_PATH, 'rb')

# creating a pdf reader objectW
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# printing number of pages in pdf file
print(len(pdfReader.pages))

PAGE_NUMBER = 1

def search_in_lines(lines, text_to_find):
    """Function printing the found price

    Args:
        lines (string[]): lines of text to search
        text_to_find (string): word to find in line
    """
    for line in lines:
        found_line = line.find(text_to_find)
        if found_line != -1:
            return line[len(line) - 8:len(line)]

def create_xlsx_file(text, value):
    """Function to create xlsx files

    Args:
        text (string): text to fill first cell
        value (string): value to fill second cell 
    """
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('test.xlsx')

    # The workbook object is then used to add new
    #worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', text + ':')
    worksheet.write('B1', value)
    workbook.close()

# extracting text from pages
# TODO: abstract this code in a new function
for page in pdfReader.pages:
    print('PAGE: ', PAGE_NUMBER)
    text_split_in_lines = page.extract_text().splitlines()
    print(text_split_in_lines)
    # Creating text to find in pdf
    TEXT_TO_FIND = 'Salario convenio'
    result = search_in_lines(text_split_in_lines, TEXT_TO_FIND)
    print(result)
    if result:
        create_xlsx_file(TEXT_TO_FIND, result)
    else:
        print('text not found in page:', PAGE_NUMBER)
    PAGE_NUMBER += 1

# closing the pdf file object
pdfFileObj.close()
