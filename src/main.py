import re
from utils import read_pdf_file
from utils import pdf_to_text_file
from utils import list_of_obj
from utils import list_to_dict

# Converts pdf file in to a string
pdfFile = read_pdf_file.read_pdf_file('statement.pdf', 2)
# If text file doesnt exist creates a new file
# Parses the pdf string and converts it in to list(array) of words
pdf_to_text_file.pdf_to_text_file(pdfFile)

convertedTextFile = open('newTextFile.txt', 'r')
# reads the string out of the new file
strFile = convertedTextFile.readlines()
# length of the string in the file
textFileLength = len(strFile)

# regex to match date format
purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')

# find the first date in the file
foundDate = purchaseDateRegex.findall(str(pdfFile))

# takes in a string and converts it to arr of words
listOfObj = list_of_obj.list_of_obj(strFile, foundDate, textFileLength)

# takes in a list(array) and returns a dict(obj)
totalOfAmounts = list_to_dict.list_to_dict(listOfObj)

# show key: value pairs
for i, j in totalOfAmounts.items():
    print(i, j)
