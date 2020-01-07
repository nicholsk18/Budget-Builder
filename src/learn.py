import PyPDF2
import re

# regex to match date format
purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')

pdfFileObj = open('statement.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

content = ''
for i in range(0, pdfReader.numPages):
    content += pdfReader.getPage(i).extractText()

# find the first date in the file
foundDate = purchaseDateRegex.findall(content)
print(foundDate)
print(content.find('Previous Balance'))
print(content)
pdfFileObj.close()