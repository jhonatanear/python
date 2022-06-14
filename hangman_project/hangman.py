import random
import string
import os

from data import data
from art import images


def hangman():
    word = random.choice(data).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    beginning = 0
    end = 6

    lives = 6 

    while len(word_letters) > 0 and lives > 0:
        print('\nTe quedan ' + str(lives) + ' vidas. Haz intentado con las siguientes letras:' , ' '.join(sorted(used_letters)))  
        print(images[beginning])
        word_list = [letter if letter in used_letters else '_' for letter in word]       
        print('Palabra actual: ', ''.join(word_list))
        user_letter = input('Digita una letra:').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else: 
                lives -= 1
                beginning += 1
                print('La letra no se encuentra en la palabra.')
        
        elif user_letter in used_letters:
            lives -= 1
            beginning += 1
            print('Ya intentantes con esta letra. Intenta nuevamente.') 
        
        else:
            print('Letra incorrecta. Intenta nuevamente.')
    
    if lives == 0 and end == 6:
        os.system('clear')
        print('Perdiste. La palabra era: ' + word + ' Juego finalizado.')
    
    else:
        os.system('clear')
        print('Ganaste, la palabra es: .' + word)


def run():
    hangman()


if __name__ == '__main__':
    run()