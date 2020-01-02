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
