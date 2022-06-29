import random

from data import *


def password_generator(len):

    character = uppercase + lowercase + numbers + symbols

    password = []

    for i in range(len):
        character_random = random.choice(character)
        password.append(character_random)

    password = ''.join(password)
    return password 


def run():
    print('Bienvenido a tu generador de contraseñas')
    while True:
        try:
            len = int(input('\nIngrese la longitud de su contraseña: '))
        
        except ValueError:
            print('La longitud de la contraseña debe ser un numero entero. Intente nuevamente.')
            continue

        if len < 8:
            print('No se puede elegir una contraseña con una longitud menor a 8 caracteres.'
            +' Intente de nuevo.')
        else: 
            password = password_generator(len)
            print('Tu nueva contraseña es: ' + password)
            break


if __name__ == '__main__':
    run()