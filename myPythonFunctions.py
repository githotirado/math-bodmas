# libraries to import
from random import randint
from os import remove, rename
import pathlib

scorestxt = pathlib.Path('./math-bodmas/userScores.txt')
scorestmp = pathlib.Path('./math-bodmas/userScore.tmp')

def getUserPoint(userName):
    '''Get the user point from scorestxt file if user 'userName' exists in the file.
    If 'userName' exists in the file, return code is score; if user does not yet exist,
    create the file and return code -1.
    '''
    try:
        with open(scorestxt) as scoresFile:
            for line in scoresFile:
                content = line.strip('\n').split(',')
                if userName == content[0]:
                    scoresFile.close()
                    return content[1]
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
                    # Decision to append scores file or to update existing entry
                    if userName != content[0]:
                        scoreTmp.write(f"{content[0]}, {content[1]}\n")
                    else:
                        scoreTmp.write(f"{userName}, {score}\n")
        # Close the files, remove original file, rename tmp file to original file
        scoresFile.close()
        scoreTmp.close()
        remove(scorestxt)
        rename(scorestmp, scorestxt)

## Generate the math question
def genQuestion():
    '''Generate the two random lists containing the operands and operators.
    Show resulting math question.  Prompt user for answer. Compare to actual results
    and award the player appropriately.
    '''
    # Set up the variables containers
    operandList  = [0, 0, 0, 0, 0]
    operatorList = ['','','','']
    operatorDict = { 1: '+', 2: '-', 3: '*', 4: '**', 5: '/'}

    # Populate operand list
    for n in range(len(operandList)):
        operandList[n] = randint(0, 9)
        
    # Populate operator list, avoiding two consecutive '**'
    for m in range(len(operatorList)):
        if (m > 0 and operatorList[m - 1] == '**'):
            # Instead of the next 'while' loop, make the 'randint' function
            # return any operator except '**' by excluding operatorDict[4]
            # operatorList[m] = operatorDict[randint(1, 3)]
            while (operatorList[m] == ''  or  operatorList[m] == '**'):
                operatorList[m] = operatorDict[randint(1, len(operatorDict))]
        else:
            operatorList[m] = operatorDict[randint(1, len(operatorDict))]
    
    # Tack on one final '' to operatorList to help with printing question in loop
    operatorList.append('')

    # Show the math question
    questionString = ''
    for p in range(len(operandList)):
        questionString += f"{operandList[p]}{operatorList[p]}"
    result = round(eval(questionString))
    questionString = questionString.replace('**', '^')
    print(f"{questionString} = ")
    while True:
        try:
            userResp = int(input("Enter your guess: "))
            if userResp == result:
                print(f"Correct!  You score a point.")
                return 1
            else:
                print(f"Incorrect.  Correct answer is {result}. No points awarded.")
                return 0
        except:
            print(f"Error, not an integer.  Please try again.") 


# Main section (executed only library is called from command line)
if __name__ == "__main__":
    # myUser = input("Enter a user name: ")
    # myScore = input("Enter that user score: ")
    # return_value = getUserPoint(myUser)
    # print(f"Returned value is: {return_value}")
    # updateUserPoints(True, myUser, myScore)
    print(genQuestion())