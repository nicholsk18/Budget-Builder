# This function is used to create a dictionary
# The numbers get striped of special char and converted to a float
# if the key already exist in dict add the new value to old
# if it does not creates a new key: value pair


def list_to_dict(listOfObj):
    # creating/adding places and total amount spend
    totalOfAmounts = {}

    for i in range(0, len(listOfObj), 3):
        if '- $' in listOfObj[i+2]:
            newNum = float(listOfObj[i+2].replace('- $', ''))
            newNum = -newNum
        else:
            newNum = float(listOfObj[i+2].replace("$", ""))
        if listOfObj[i+1] in totalOfAmounts:
            totalOfAmounts[listOfObj[i+1]] += newNum
        else:
            totalOfAmounts[listOfObj[i+1]] = newNum

    return totalOfAmounts
