# libraries to import
from random import randint
from os import remove, rename
import pathlib

scorestxt = pathlib.Path('./math-bodmas/userScores.txt')

def getUserPoint(userName):
    try:
        with open(scorestxt) as scoresFile:
            # print(f"Opened {scorestxt}.")
            for line in scoresFile:
                content = line.strip('\n').split(',')
                # print(f"File '{content[0]}' vs Entry '{userName}'")
                if userName == content[0]:
                    print(f"{content[0]} {content[1]}")
                    scoresFile.close()
                    return 0
    except IOError:
        with open(scorestxt, "w") as scoresFile:
            print(f"File {scorestxt} does not exist.  Creating it.")
                  
    scoresFile.close()
    return -1
    
# Main section
if __name__ == "__main__":
    myUser = input("Enter a user name: ")
    return_value = getUserPoint(myUser)
    print(f"Returned value is: {return_value}")