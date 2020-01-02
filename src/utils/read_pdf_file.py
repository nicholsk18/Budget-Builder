# This function converts pdf file
# Return a string of the content
# replaces "\n" with "  -- " to track end of the line
# ^ might not be needed

import PyPDF2


def read_pdf_file(pdfFile, page):
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    content = pdfReader.getPage(page).extractText()
    # created to format the .txt file to out but down
    content = content.replace('\n', ' -- ')
    return content
