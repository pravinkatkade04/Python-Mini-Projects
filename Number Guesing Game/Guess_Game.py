
import random 

Number = random.randint(1,10)

guess = int(input("\n Guess a Number "))

if guess==Number :
    print("You win ! ")
else :
    print("Try Again !")