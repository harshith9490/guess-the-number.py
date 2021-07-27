#guess the number
import random

import time

if (time.strftime("%p",time.localtime()))=='AM':

    print("Hi Good Morning ,\n welcome to guess the number game\n if you have guess correct number your score will be increased with 4 points \n if you have guessed wrong number the score will be decrease -1")

else:

    print("Hi Good Afternoon ,\n welcome to guess the number game\n if you have guess correct number your score will be increased with 4 points \n if you have guessed wrong number the score will be decrease -1")
    

d=int(input("enter the range to guess the number : "))

score=0

r=random.randint(1,d)

guess=0

while(guess!=r):

    guess=int(input('enter the number : '))

    if guess < r:

        print("the guess number is low , try again")

        score=score-1

    elif guess > r:

        print("the guess number is high  , try again")

        score=score-1

    elif guess==r:

        print("Thats right you have guessed the number")

        score=score+4

print("score is ",score)
