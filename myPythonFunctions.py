# libraries to import
from random import randint
from os import remove, rename
import pathlib

scorestxt = pathlib.Path('./math-bodmas/userScores.txt')
scorestmp = pathlib.Path('./math-bodmas/userScore.tmp')

def getUserPoint(userName):
    '''Get the user point from scorestxt file if user 'userName' exists in the file.
    If 'userName' exists in the file, return code is 0; if user does not yet exist,
    create the file and return code -1.
    '''
    try:
        with open(scorestxt) as scoresFile:
            # print(f"Opened {scorestxt}.")
            for line in scoresFile:
                content = line.strip('\n').split(',')
                # print(f"File '{content[0]}' vs Entry '{userName}'")
                if userName == content[0]:
                    # print(f"{content[0]} {content[1]}")
                    scoresFile.close()
                    return 0
    except IOError:
        with open(scorestxt, "w") as scoresFile:
            print(f"File {scorestxt} does not exist.  Creating it.")
                  
    scoresFile.close()
    return -1

def updateUserPoints(newUser, userName, score):
    '''Update the user score file using a temp file to reconstruct the file.
    If the user is new (newUser=True), append the user to the file; if the 
    user exists (newUser=False), then when building temp file for that user
    insert the latest score for the user, rename to original file name.
    '''
    if newUser:
        with open(scorestxt, "a") as scoresFile:
            scoresFile.write(f"{userName}, {score}\n")
        scoresFile.close()
    else:
        with open(scorestxt) as scoresFile:
            with open(scorestmp, "w") as scoreTmp:
                for line in scoresFile:
                    content = line.strip('\n').split(',')
                    content[1] = content[1].strip()
                    # Decision to append or to update
                    if userName != content[0]:
                        scoreTmp.write(f"{content[0]}, {content[1]}\n")
                    else:
                        scoreTmp.write(f"{userName}, {score}\n")
        # Close the files, remove original file, rename tmp file to original file
        scoresFile.close()
        scoreTmp.close()
        remove(scorestxt)
        rename(scorestmp, scorestxt)

    
# Main section (executed only library is called from command line)
if __name__ == "__main__":
    myUser = input("Enter a user name: ")
    myScore = input("Enter that user score: ")
    return_value = getUserPoint(myUser)
    print(f"Returned value is: {return_value}")
    updateUserPoints(True, myUser, myScore)