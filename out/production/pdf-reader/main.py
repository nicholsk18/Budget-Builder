import PyPDF2

pdfFileObj = open('travel-form-1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)