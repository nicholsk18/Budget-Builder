import re
import sys
from utils import read_pdf_file
from utils import pdf_to_text_file
from utils import list_of_obj
from utils import list_to_dict

# input file that is a pdf
inFile = sys.argv[1]

# user named text file
print("What would you like the output text file to be?")
userTextFile = input()

# Converts pdf file in to a string
pdfFile = read_pdf_file.read_pdf_file(inFile, 2)
# If text file doesnt exist creates a new file
# Parses the pdf string and converts it in to list(array) of words
pdf_to_text_file.pdf_to_text_file(pdfFile, userTextFile)

convertedTextFile = open(userTextFile, 'r')
# reads the string out of the new file
strFile = convertedTextFile.readlines()
# length of the string in the file
textFileLength = len(strFile)

convertedTextFile.close()

# regex to match date format
purchaseDateRegex = re.compile(r'([A-Z][a-z][a-z] \d+)')

# find the first date in the file
foundDate = purchaseDateRegex.findall(str(pdfFile))

# takes in a string and converts it to arr of words
listOfObj = list_of_obj.list_of_obj(strFile, foundDate, textFileLength)

# takes in a list(array) and returns a dict(obj)
totalOfAmounts = list_to_dict.list_to_dict(listOfObj)

# rewrites the file with new json like data
with open(userTextFile, 'w') as userFile:
    # show key: value pairs
    for i, j in totalOfAmounts.items():
        userFile.write(i + ": " + str(j) + '\n')

    userFile.close()

# with open(userTextFile, 'r') as readingFile:
#     lines = readingFile.readlines()
#     for i in lines:
#         print(lines[i])

    # readingFile.close()
