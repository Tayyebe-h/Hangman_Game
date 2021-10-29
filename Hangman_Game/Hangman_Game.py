import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

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

 for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        if display[position] == "_":
             display[position] = letter
        else:
            print("You've already guessed "+ guess)


 if guess not in chosen_word:
      print("You guessed "+ guess + ", that is not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")
 
 print(f"{' '.join(display)}")
 
 if not "_" in display:
     end_of_game = True
     print("You win.")

 print(stages[lives]) 
 

