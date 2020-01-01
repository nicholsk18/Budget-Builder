import PyPDF2
import re
import os


def readPdfFile(pdfFile, page):
    pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    content = pdfReader.getPage(page).extractText()
    content = content.replace('\n', ' -- ')

    return content


def pdfToTextFile(content):
    if os.stat("newTextFile.txt").st_size != 0:
        print("already converted")
    else:
        # create new file that contains pdf string
        textFile = open('newTextFile.txt', 'a')
        textFile.writelines(str(content.encode('ascii', 'ignore')))
        textFile.close()

        # Format str to break up each " -- "in to new line
        textFile = open('newTextFile.txt', 'r')
        strFile = textFile.readlines()
        formatStr = str(strFile).replace(' -- ', '\n')
        textFile.close()

        # over write the old file with new formated string
        textFile = open('newTextFile.txt', 'w')
        textFile.writelines(formatStr)
        textFile.close()


pdfFile = readPdfFile('statement.pdf', 2)
pdfToTextFile(pdfFile)

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

# for x in totalOfAmounts.values():
print(totalOfAmounts)
