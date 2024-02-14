import random
import hangman_words
import hangman_acii

word_list = hangman_words.word_list

print(hangman_acii.hangman_title)

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

chosen_word = random.choice(word_list)

display = []
lives = 0

for _ in range(len(chosen_word)):
    display += "_"
print(display)


def update_letter():
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if  letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        global lives
        lives += 1
        print(stages[lives])
        if(lives == 6):
            print("You Lose")


end_of_game = False

# print(f"lives {lives}")
while not end_of_game and lives < 6:
    if "_" in display:
        print(display)
        update_letter()
        
    else:
        end_of_game = True
        print("You Win")









