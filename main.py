"""
Programme par Elouan Cassoudebat--Arcila, Groupe 407
programme ayant pour but de trouver un nombre choisi de manière aléatoire choisi par l'ordinateur entre deux bornes
choissi par l'utilisateur
"""


from random import randint


def get_int_input(phrase: str) -> int:
    """
    s'assure que le nombre du joueur soit bien un nombre
    """
    try:
        nombre = int(input(phrase))
    except ValueError:
        nombre = get_int_input(phrase)
    return nombre


def play_game():
    """
    Choisi le nombre aléatoire et permet au joueur de le deviner (Le jeu)
    """
    nb_essai = 0
    nb_un = input("Choissisez la borne la plus petite:\n -->")  # la borne une (plus petite)
    nb_deux = input("Choissisez la borne la plus grande:\n -->")  # la borne deux (plus grande)
    nb_choisi = randint(int(nb_un), int(nb_deux))  # le nombre aléatoire a trouver
    print("J’ai choisi un nombre au hasard entre", nb_un, "et", nb_deux, "Vous de le deviner...")
    while nb_choisi != (nombre_joueur := get_int_input("Entrez votre essai\n -->")):
        nb_essai += 1
        if nombre_joueur > nb_choisi:
            print("Mauvaise réponse, le nombre est plus petit que l\'essai")

        elif nombre_joueur < nb_choisi:  # previent l'utilisateur que le nombre est trop petit
            print("Mauvaise réponse, le nombre est plus grand que l\'essai")

    nb_essai += 1  # previent l'utilisateur que le nombre est le bon
    print("Bravo! Bonne réponse")
    print("Vous avez réussi en ", nb_essai, "essai(s)")


while True:
    play = input("\n Voulez-vous jouer (o/n)?\n -->")
    if play == "n":
        print("ah ok...")
        break
    if play == "o":
        play_game()
