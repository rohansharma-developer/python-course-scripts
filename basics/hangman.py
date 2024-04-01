import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

lives = 5

chosen_word = random.choice(word_list)

print(chosen_word)

display = []
for letter in chosen_word:
    display += "_" 
print(display)

end = False

while not end:

    guess = input("Guess a letter: \n").lower()


    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if guess == letter:
            display[pos] = letter
    print(display)

    if "_" not in display:
        end = True
        print("You win!")