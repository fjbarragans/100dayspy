#Hangman
word_list = ["amarillo", "azul", "verde", "rojo", "morado", "naranja", "café", "negro", "blanco"]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

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

print(f"Welcome to hangman game\n{logo}")
import random
from replit import clear

chosen_word = random.choice(word_list)

guesslist = []
word_lenght = len(chosen_word)
for letter in range(word_lenght):
    guesslist += "_"
print(f"{''.join(guesslist)}")

end = False
lives = 6
while not end:
  guess = input("Guess a letter: ").lower()

  clear()

  if guess in guesslist:
    print(f"You have already guessed {guess}")
  else:
    for i in range(word_lenght):
      letter = chosen_word[i]
      if letter == guess:
        guesslist[i]= guess
    
    if guess not in chosen_word:
      lives -= 1
      print(f"You guess {guess}. It is not in the word")
    
  print(f"{''.join(guesslist)}")

  if "_" not in guesslist:
      end = True
      print("You win")
  elif lives == 0:
      end = True
      print("You lose")
  
  print(stages[lives])