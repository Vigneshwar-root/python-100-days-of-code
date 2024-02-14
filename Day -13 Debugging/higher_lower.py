import json
from random import randint
from art import *



with open('data.json') as game_json:
    file_contents = json.load(game_json)
    game_data = file_contents["objects"]

def compare_followers(score):
    a = randint(1,1561)
    # print(game_data[a])
    print(f"Compare A: {game_data[a]['name']}")
    print(vs)
    b = randint(1,1561)
    if b == a:
        b = randint(1,1561)
    print(f"Compare B: {game_data[b]['name']}")
    compare_result = ""
    if game_data[a]['value'] > game_data[b]['value']:
        compare_result = 'A'
    else:
        compare_result = 'B' 

    user_response = input(f"Who has more followers? Type 'A' or 'B'\n")
    if(user_response == compare_result):
        score += 1
        print(f"\nYou are right! Current Score: {score}\n")
        compare_followers(score)
    else:
        print(f"\nGame Over! Final Score: {score}")
        response = input("Do you wanna play again ? Type 'Y' to continue or any other key to end the game\n")
        if response.lower() == 'y':
            compare_followers(0)
        else:
            return False

# print(len(file_contents["objects"]))

print(logo)
current_score = 0
game_should_continue = True
while game_should_continue:
    game_should_continue = compare_followers(current_score)


