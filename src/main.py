import re
from utils import read_pdf_file
from utils import pdf_to_text_file

# Converts pdf file in to a string
pdfFile = read_pdf_file.read_pdf_file('statement.pdf', 2)
# If text file doesnt exist creates a new file
# Parses the pdf string and converts it in to list(array) of words
pdf_to_text_file.pdf_to_text_file(pdfFile)

convertedTextFile = open('newTextFile.txt', 'r')
fileLines = convertedTextFile.readlines()
# print(fileLines)
textFileLength = len(fileLines)

purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')
foundDate = purchaseDateRegex.findall(str(pdfFile))


# creating/adding places and total amount spend
totalOfAmounts = {}

listOfObj = []

for i in range(0, textFileLength):
    for j in range(0, len(foundDate)):
        if fileLines[i].rstrip() == foundDate[j]:
            listOfObj.append(fileLines[i].rstrip())
            if fileLines[i+2].rstrip().startswith('$'):
                listOfObj.append((fileLines[i+1].rstrip()))
                listOfObj.append(fileLines[i+2].rstrip())
            else:
                listOfObj.append(fileLines[i+1].rstrip() + " " + fileLines[i+2].rstrip())
                listOfObj.append(fileLines[i+3].rstrip())
            break

for i in range(0, len(listOfObj), 3):
    newStr = ''
    if '- $' in listOfObj[i+2]:
        newNum = float(listOfObj[i+2].replace('- $', ''))
        newNum = -newNum
    else:
        newNum = float(listOfObj[i+2].replace("$", ""))
    # print(newStr)
    if listOfObj[i+1] in totalOfAmounts:
        totalOfAmounts[listOfObj[i+1]] += newNum
    else:
        totalOfAmounts[listOfObj[i+1]] = newNum

for i, j in totalOfAmounts.items():
    print(i, j)
