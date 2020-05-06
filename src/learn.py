import PyPDF2
import re
import os
import sys

# regex to match date format
purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')

pdfFileObj = open('statement.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

content = ''
for i in range(0, pdfReader.numPages):
    content += pdfReader.getPage(i).extractText()

# find the first date in the file
foundDate = purchaseDateRegex.findall(content)
# print(foundDate)
# print(content.find('Previous Balance'))
# print(content)
pdfFileObj.close()


def pdf_to_text_file(content, userTextFile):
    textFile = open(userTextFile, 'a')
    if os.stat(userTextFile).st_size != 0:
        print("already converted")
    else:
        # create new file that contains pdf string
        textFile.writelines(str(content.encode('ascii', 'ignore')))
        textFile.close()

        # Format str to break up each " -- "in to new line
        textFile = open(userTextFile, 'r')
        strFile = textFile.readlines()
        formatStr = str(strFile).replace(' -- ', '\n')
        textFile.close()

        # over write the old file with new formated string
        textFile = open(userTextFile, 'w')
        textFile.writelines(formatStr)
        textFile.close()


def list_of_obj(strFile, foundDate, strFileLength):
    listOfObj = []

    for i in range(0, strFileLength):
        for j in range(0, len(foundDate)):
            # looks for the first date,
            # Matches with regex of all the dates
            if strFile[i].rstrip() == foundDate[j]:
                # Adds date to a list
                listOfObj.append(strFile[i].rstrip())
                # check to see if next string is a dollar amount
                # if it is adds it next
                if strFile[i+2].rstrip().startswith('$'):
                    listOfObj.append((strFile[i+1].rstrip()))
                    listOfObj.append(strFile[i+2].rstrip())
                else:
                    # if next isnt an amount value
                    # adds two str together and goes to third value
                    listOfObj.append(strFile[i+1].rstrip() + " " + strFile[i+2].rstrip())
                    listOfObj.append(strFile[i+3].rstrip())
                break

    return listOfObj



pdf_to_text_file(content, 'myfile.txt')
convertedTextFile = open('myfile.txt', 'r')
# reads the string out of the new file
strFile = convertedTextFile.readlines()
# length of the string in the file
textFileLength = len(strFile)

convertedTextFile.close()
# regex to match date format
purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')

# find the first date in the file
foundDate = purchaseDateRegex.findall(str('myfile.txt'))

# takes in a string and converts it to arr of words
listOfObj = list_of_obj(strFile, foundDate, textFileLength)

# takes in a list(array) and returns a dict(obj)
# totalOfAmounts = list_to_dict.list_to_dict(listOfObj)
print(listOfObj)