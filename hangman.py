print(
"""

'   .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
'  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
'  | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
'  | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
'  | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
'  | |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
'  | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
'  | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
'  | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
'  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

BIENVENIDO AL JUEGO DEL AHORCADO!!
*Deberás adivinar la palabra secreta antes que se te agoten las oportunidades.
*Cada oportunidad perdida es un paso más hacia la derrota.
*Disfruta y ve con cuidado

""")

import random

def hangman():
    intentos=5
    acierto=0
    lista=[]
    final=""

    with open ("palabras.txt", "r", encoding='utf-8') as f:
        for i in f:
            lista.append(i.rstrip("\n"))

    palabra_aleatoria = random.choice(lista)

    adivina =["_" for i in palabra_aleatoria]
    print(""" 
        Bienvenido/a al juego del ahorcado 
        la palabra que debes adivinar es """  +"_ "*len(palabra_aleatoria)
        +"Tienes " +str(intentos)+" intentos")
    while(True):

        letra=input("Ingresa una letra ").lower()
        if(len(letra)>=2 or letra.isalpha==False):
            letra=""
            print(" Has ingresado un caracter inválido")
            continue

        for count, i in enumerate(palabra_aleatoria):
            if letra == i:
                adivina[count]=letra
                acierto+=1
        print("acertaste "+ str(acierto)+" veces la letra "+ letra)
        acierto=0
        if letra not in palabra_aleatoria:
            intentos -=1
            print("Te has equivocado, te quedan "+ str(intentos)+ " intentos")
        
        for i in adivina:
            print(i , end=" ")
            final+=i
        if final == palabra_aleatoria:
            print("Has ganado, la palabra correcta es "+final)
            break
        if intentos ==0:
            print("Has perdido, mejor suerte la próxima. La palabra correcta era "+ palabra_aleatoria)
            break
        final=""        


if __name__ == '__main__':
    hangman()