# This function creates a new file
# Checks to see if file already has content
# if not writes to file then
# reads file and changes " -- " with "\n" for the outcome look of .txt file
# writes new formated string back to the file overriding old file

import os
import sys
sys.path.append("./utils/")


def pdf_to_text_file(content):
    textFile = open('newTextFile.txt', 'a')
    if os.stat("newTextFile.txt").st_size != 0:
        print("already converted")
    else:
        # create new file that contains pdf string
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
