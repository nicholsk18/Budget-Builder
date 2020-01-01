import PyPDF2


def read_pdf_file(pdfFile, page):
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    content = pdfReader.getPage(page).extractText()
    content = content.replace('\n', ' -- ')
    return content

