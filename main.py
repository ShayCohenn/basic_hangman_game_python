import random
from ascii_art import stages
from random_words import words_list

chosen_word = random.choice(words_list)

lives = len(stages)

wrong_letters = []

from ascii_art import logo
print(logo)

#Create blanks
display = []
for _ in chosen_word:
    display += "_"

while True:
    guess = input("Guess a letter: ").lower()
    if len(guess) == 1:
      if guess in display:
          print(f"You've already guessed {guess}")
  
      #Check guessed letter
      for letter in chosen_word:
          if letter == guess:
              display[chosen_word.index(letter)] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          lives -= 1
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          wrong_letters.append(guess)
          print(stages[lives])
          if lives == 0:
              print("Game over, You lost...")
              break
      else:
         print(stages[lives])
  
      #Join all the elements in the list and turn it into a String.
      print(' '.join(display))
      print(f"Incorrect letters: {','.join(wrong_letters)}")
      print(f"{lives}/{len(stages)} lives remaining.")
  
      #Check if user has got all letters.
      if "_" not in display:
          print("You win.")
          break
    else:
      print("Please enter a single letter.")