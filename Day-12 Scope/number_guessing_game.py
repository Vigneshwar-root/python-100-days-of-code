from random import randint
from logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess,answer):
    if guess > answer:
        print("Too High.")
        return ""
    elif guess < answer:
        print("too Low")
        return ""
    else:
        print(f"You got it! The answer was {answer}.")
        return "success"

def set_difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    if user_input == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS


print(""""
 _____ ___  _ ____  _____   ____  ____  _      _____ _____  _     _  _      _____  
/__ __\\  \///  __\/  __/  / ___\/  _ \/ \__/|/  __//__ __\/ \ /|/ \/ \  /|/  __/  
  / \   \  / |  \/||  \    |    \| / \|| |\/|||  \    / \  | |_||| || |\ ||| |  _  
  | |   / /  |  __/|  /_   \___ || \_/|| |  |||  /_   | |  | | ||| || | \||| |_//  
  \_/  /_/   \_/   \____\  \____/\____/\_/  \|\____\  \_/  \_/ \|\_/\_/  \|\____\  
                                                                                   
""")
print("Welcome to the Number guessing game! \nI'thinking of a number between 1 and 100'\n")
answer = randint(1,100)
turns = set_difficulty()
status = ""
while turns > 0:
    print(f"You have {turns} attempts remaining to guess the number")
    guess = int(input("Make a guess:"))
    status = check_answer(guess,answer)
    if status == 'success':
        turns = 0
    else:
        turns -= 1
        if turns == 0:
            print("You have run out of guesses, you lose")



