#write a program that prompts user to enter hours and rate of pay
#take into account 1.5 times overtime over 40 hoursimport random
#Program 1

import random

program = True
while program:
    print("Hi employee, please enter your work hours and rate of pay")
    hours = int(input("please enter your hours here:"))
    pay = int(input("please enter your pay here:"))
    if pay > 1000 or pay < 6 or hours > 168 or hours < 1:
        print("impossible, please reenter your details")
    else:
        program = False

print("Thank you for entering your details ... calculating pay")

if hours <= 40:
    total = (hours*pay)
elif hours > 40:
    total = (40*pay) + ((hours-40)*pay*1.5)

print(f"Your total weekly paycheck is {total} pounds")

#asks the user a number
#if the number is odd print odd, if its even prink even
#Program 2
number = int(input("please enter a number:"))

if number%2 == 0:
    print("the number is even !")
if number%2 != 0:
    print("the number is odd !")

#write a program that has a number variable assigned between 1-20.
#give user 3 guesses for correct number
# make number random
# clue each time higher or lower
#Program 3

print("Let's play a guessing game, pick a number between 1 and 20:")
n = random.randint(1,21)

numberguess = 4
failurecount = 0
wincount = 0
while numberguess > 0:
    g1 = int(input("What is your guess:"))
    if g1 < 1 or g1 > 20:
        print("That guess is out of range, it must be between 1 and 20")
        print(f"guesses remaining: {numberguess-1}")
    elif g1 == n:
        print(f"That's right it was {n}")
        wincount += 1
        print(f"guesses remaining: {numberguess - 2}")
        print(f"you have won {wincount} times, you have lost {failurecount} times")
        q = input("would you like to play again? (y/n)")
        if q == "y":
            n = random.randint(1, 21)
            numberguess = 4
        else:
            break
    elif g1 > n:
        print("thats too high !")
        print(f"guesses remaining: {numberguess - 2}")
        numberguess -= 1
    elif g1 < n:
        print("that's too low !")
        print(f"guesses remaining: {numberguess - 2}")
        numberguess -= 1
    if numberguess == 1:
        print("you failed")
        failurecount += 1
        print(f"you have won {wincount} times, you have lost {failurecount} times")
        q = input("would you like to play again? (y/n)")
        if q == "y":
            n = random.randint(1, 21)
            numberguess = 4
        else:
            break

#write a program tha prints every number 1 to 100
#multiples of 3 print fizz and multiples of 5 print buzz , multiples of both
#print fizzbuzz for both
#Program 4

number = 0

while number < 100:
    number += 1
    if number%3 == 0 and number%5 != 0:
        print("fizz")
    elif number%5 == 0 and number%3 !=0:
        print("buzz")
    elif number%5 ==0 and number%3 ==0:
        print("fizzbuzz")
    else:
        print(number)
print("END OF PROGRAMS")


