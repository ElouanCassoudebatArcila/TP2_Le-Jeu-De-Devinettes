'''
programme ayant pour but de trouver un nombre choissi de manière aléatoire entre deux bornes choissi par l'utilisateur
'''


from random import randint

def  get_int_input(phrase:str)->int:
    try:
        nombre = int(input(phrase))
    except ValueError:
        nombre = get_int_input(phrase)
    return nombre

def play_game():
    nb_essai = 0   #le nombre d'essai
    nb_un = input("Choissisez la borne la plus petite:\n -->")  #la borne une (plus petite)
    nb_deux = input("Choissisez la borne la plus grande:\n -->")  #la borne deux (plus grande)
    nb_choisi = randint(int(nb_un), int(nb_deux))   #le nombre aléatoire a trouver
    print (nb_choisi)
    nombre = 1000000  #le nombre a deviner
    print("J’ai choisi un nombre au hasard entre" ,nb_un, "et" ,nb_deux, "Vous de le deviner...")
    while int(nb_choisi) != int(nombre := get_int_input("Entrez votre essai\n -->")):
        nb_essai += 1
        if int(nombre) > int(nb_choisi):
            print("Mauvaise réponse, le nombre est plus petit que l\'essai")

        elif int(nombre) < int(nb_choisi):
            print("Mauvaise réponse, le nombre est plus grand que l\'essai")

        if int(nombre) == int(nb_choisi):
            print("Bravo! Bonne réponse")
            print("Vous avez réussi en ", nb_essai, "essai(s)")


while True:
    play = input("\n Voulez-vous jouer (o/n)?\n -->")
    if play == ("n"):
            print("ah ok...")
            break
    if play == ("o"):
            play_game()
