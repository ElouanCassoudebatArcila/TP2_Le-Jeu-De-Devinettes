from random import randint
nb_essai = 0   #le nombre d'essai
nb_choisi = randint(0, 100)   #le nombre aléatoire a trouver
nombre = 101   #le nombre deviné
print("J’ai choisi un nombre au hasard entre 0 et 100. Vous de le deviner...")
while int(nb_choisi) != int(nombre):
    nombre = input("Entrez votre essai :")
    nb_essai += 1
    if int(nombre) > int(nb_choisi):02.1#
    print("Mauvaise réponse, le nombre est plus petit que l essai")

    elif int(nombre) < int(nb_choisi):
    print("Mauvaise réponse, le nombre est plus grand que l essai")

    elif int(nombre) == int(nb_choisi):
    print("Bravo! Bonne réponse")
    print("Vous avez réussi en ", nb_essai, "essai(s)")
    play_again = input("Voulez-vous faire une autre partie (o/n)?")
    if play_again == ("n"):
    print("Merci et au revoir…")
    break
    elif play_again == ("o"):





