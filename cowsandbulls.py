import random

numtoguess = [random.randrange(0,10,1) for _ in range (4)]
print(numtoguess)

userinput = []

while numtoguess != userinput:
    userinput = [int(i) for i in input("Welcome to Cows and Bulls game!!! \nGuess the random 4 digit number :> ")]
    cows = 0
    bulls = 0
    counter = 0
    for i in userinput:
        if userinput == numtoguess:
            print('Congrats you guessed it! \n The game will exit now.')
            break
        if i in numtoguess and i == numtoguess[counter]:
            bulls += 1
        elif i in numtoguess and i != numtoguess[counter]:
            cows += 1
        counter += 1
    print('Cows: ' + str(cows))
    print('Bulls: ' + str(bulls))

