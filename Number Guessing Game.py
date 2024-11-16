import random

def Guess_Game(noa,sr):
    comp_guess=random.randint(sr[0],sr[1])
    for i in range(noa,0,-1):
        user_guess=int(input("Enter your guess: "))
        if user_guess<comp_guess and i!=1:
            print("Your guess is less than my number!",i-1,"attempts left!")
        elif user_guess>comp_guess and i!=1:
            print("Your guess is more than my number!",i-1,"attempts left!")
        elif user_guess==comp_guess:
            return print("You have guessed my number in",(noa-i)+1,"attempts!")
        print()
    print("You couldnt guess my number!, it was",comp_guess,"!")

noa=int(input("Welcome to th enumber guessing game!!! Enter number of attempts you would like to have: "))
sr=eval(input("Enter the range from which I should select my number in square brackets seperating with comma:  "))
print()
Guess_Game(noa,sr)