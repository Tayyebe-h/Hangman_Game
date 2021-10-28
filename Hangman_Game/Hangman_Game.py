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


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"



while not end_of_game:
 guess = input("Guess a letter: ").lower()
 exists = False

 for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        exists = True

 if not exists:
      lives -= 1
 
 print(f"{' '.join(display)}")
 print(stages[lives]) 

 if not "_" in display:
     end_of_game = True
     print("You win.")
 if lives == 0:
      end_of_game = True
      print("You lose.")

