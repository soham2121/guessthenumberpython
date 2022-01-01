import random
number = random.randint(1, 9)
chance = 0
gameend = 0
print(number)
while chance < 5:
    guess = int(input("Guess the number: "))
    if(number == guess):
        print("You won!! :)")
        gameend = 1
        chance = 10
    else:
        chance += 1
        if(number - guess == -1 or number - guess == 1):
            print("Guess was very close")
        elif(number - guess >= -3 and number - guess <= 3):
            print("Guess was close")
        else:
            print("guess was far")
        print("Guesses left: ", 5-chance)

if(chance >= 5 and gameend == 0):
    print("You lost :( The number was - ", number)