import myPythonFunctions as mp

try:
    # Determine if the user has recorded any scores previously
    userName = input("Enter your first name: ")
    userScore = int(mp.getUserPoint(userName))
    print(f"User {userName} score is {userScore}")
    if userScore == -1:
        newUser = True
        userScore = 0
    else:
        newUser = False
    
    # Decision to continue or terminate the game
    userChoice = 0
    terminate = -1
    while userChoice != terminate:
        print("Game is active ...")
        # Run the game, add score to existing score
        userScore += mp.genQuestion()
        print(f"Your score is: {userScore}.")
        userChoice = int(input("Do you wish to continue playing? (1 [continue] or -1 [terminate]): "))
    mp.updateUserPoints(newUser, userName, userScore)
except:
    print("an exception has occurred.")
