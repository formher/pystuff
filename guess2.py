# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

from random import randint

numtoguess = list(range(1, 51))

lowest = 0
highest = 100
mid = 50

counter = 0


# print(numtoguess)
mynum = 18




while True:
    print('Is your guess ' + str(mid) + ' ?')
    userinput = str(input('Yes - for correct.\n> - if the hidden number is greater than guessed.\n< - if the hidden number is less than guessed.'))
    if userinput == '>':
        mid += 1
        counter += 1
        print('Is your guess ' + str(mid) + ' ?')

    elif userinput == '<':
        mid -= 1
        counter += 1
        print('Is your guess ' + str(mid) + ' ?')

    elif userinput == 'yes':
        print('I guess it in ' + str(counter) + ' tries. The program will exit now.')
        break

