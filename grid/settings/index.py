import random
from unicodedata import normalize, combining

# Fonction de recuperation du fichier et exportation des mots dans une liste
def fc_open(file):
    with open(file, "r", encoding='utf-8') as tf:
        lines = tf.read().split('\n')
    return fc_sort_word(lines)

# Fonction pour enlever les accents
def fc_accent(ch):
    # suppression des accents qui restent
    chnorm = normalize('NFKD', ch)
    return "".join([c for c in chnorm if not combining(c)])

# Fonction qui trie en fonction du nombre de lettres (limité à 14 lettres maximum pour un mot)
def fc_sort_word(words):
    # retire tous les accents des mots
    for ch in range(len(words)):
        words[ch] = fc_accent(words[ch])
    #
    # Melange la liste pour ne pas avoir un ordre alphabetique
    random.shuffle(words)
    #
    i = 0
    liste = [[0 for _ in range(0)] for _ in range(15)]
    while i < 15:
        for word in words:
            if len(word) == i+1:
                liste[i].append(word)
        i = i + 1
    return liste

def fc_choose_word(liste, letter_word_to_word, nb_lettre, position):
    for word in liste[nb_lettre-1]:
        if (word[position-1] == letter_word_to_word):
            number = word
            break
    if 'number' in locals():
        return (number)
    else:
        return (False)

def fc_create_liste(liste):
    # ordre de recuperation des mots de la grille : 7,3,6,1,4,2,5
    # croisements : 7 -> 3,6,1,4
    #               1 -> 2
    #               4 -> 5

    # 7 #
    # mot de base choisie aleatoirement avec longueur minimum de 3#
    if random.randint(1, 2) == 2:
        # ajoute plus de chance pour les mots de plus de 7 lettres
        len_random = random.randint(7, 12)
    else:
        len_random = random.randint(2, 12)
    seven = random.choice(liste[len_random])

    one = two = three = four = five = six = ""
    print("7 : " + seven)
    letter_seven_to_three = seven[0]
    letter_seven_to_six = seven[2]
    if len_random > 5:
        letter_seven_to_one = seven[6]
    if len_random > 11:
        letter_seven_to_four = seven[12]
    # 7 #

    # # 3 #
    # -> entre 3 et 13 lettres + milieu du mot = 1e du 7
    len_random_three = random.randint(3, 13)
    while fc_choose_word(liste, letter_seven_to_three, len_random_three, len_random_three//2+1) == False:
        len_random_three = random.randint(3, 13)
    three = fc_choose_word(liste, letter_seven_to_three, len_random_three, len_random_three//2+1)
    print(len_random_three//2+1)
    print("3 : " + three)
    print(letter_seven_to_three)
    # 3 #

    # 6 #
    # -> entre 3 et 8 lettres + 2e = 3e du 7
    len_random_six = random.randint(3, 8)
    while fc_choose_word(liste, letter_seven_to_six, len_random_six, 2) == False:
        len_random_six = random.randint(3, 8)
    six = fc_choose_word(liste, letter_seven_to_six, len_random_six, 2)
    print("5 : " + six)
    print(letter_seven_to_six)
    # 6 #

    if len_random > 5:
        # 1 #
        # -> entre 7 et 13 lettres + 7e = 7e du 7
        len_random_one = random.randint(7, 13)
        while fc_choose_word(liste, letter_seven_to_one, len_random_one, 7) == False:
            len_random_one = random.randint(7, 13)
        one = fc_choose_word(liste, letter_seven_to_one, len_random_one, 7)
        print("1 : " + one)
        print(letter_seven_to_one)
        letter_one_to_two = one[1]
        # 1 #

        # condition pour la grille numero 2 pour ajouter de l'aleatoire
        if random.randint(1, 3) != 2:
            # 2 #
            # -> entre 3 et 7 lettres + 5e = 2e du 1
            len_random_two = random.randint(3, 7)
            while fc_choose_word(liste, letter_one_to_two, len_random_two, 3) == False:
                len_random_two = random.randint(3, 7)
            two = fc_choose_word(liste, letter_one_to_two, len_random_two, 3)
            print("2 : " + two)
            print(letter_one_to_two)
            # 2 #

        # condition pour la grille numero 3 pour ajouter de l'aleatoire
        if random.randint(1, 3) == 2:
            three = ""

    if len_random > 11:
        # 4 #
        # -> entre 3 et 13 lettres + milieu = 13e du 7
        len_random_four = random.randint(3, 13)
        while fc_choose_word(liste, letter_seven_to_four, len_random_four, len_random_four//2+1)== False:
            len_random_four = random.randint(3, 13)
        four = fc_choose_word(liste, letter_seven_to_four, len_random_four, len_random_four//2+1)
        print("4 : " + four)
        print(letter_seven_to_four)
        # 4 #

        if len_random_four > 6:
            letter_four_to_five = four[len_random_four//2+3]
            # 5 #
            # -> entre 2 et 5 lettres + dernier = 7e du 4
            len_random_five = random.randint(2, 5)
            while fc_choose_word(liste, letter_four_to_five, len_random_five, len_random_five) == False:
                len_random_five = random.randint(2, 5)
            five = fc_choose_word(liste, letter_four_to_five, len_random_five, len_random_five)
            print("5 : " + five)
            print(letter_four_to_five)
            # 5 #

        # condition pour la grille numero 6 pour ajouter de l'aleatoire
        if random.randint(1, 3) == 2:
            six = ""

    return [one, two, three, four, five, six, seven]


def fc_liste_to_grille(liste_final):
    grille = [[' ' for _ in range(14)] for _ in range(13)]
    i = 0
    position_letter = [0, 0, 0, 0, 0, 0, 0]
    while i < 14:
        j = 0
        while j < 14:
            # 1 #
            k = 0
            if j == 6:
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k]+1
            # 1 #

            # 2 #
            k = k + 1
            if i == 1 and j > 3:
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k]+1
            # 2 #

            # 3 #
            k = k + 1
            if j == 0 and i >= (6 - len(liste_final[k])//2):
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k] + 1
            # 3 #

            # 4 #
            k = k + 1
            if j == 12 and i >= (6 - len(liste_final[k])//2):
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k] + 1
            # 4 #

            # 5 #
            k = k + 1
            if j > (12 - len(liste_final[k])) and i == 9:
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k] + 1
            # 5 #

            # 6 #
            k = k + 1
            if j == 2 and i > 4:
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k] + 1
            # 6 #

            # 7 #
            k = k + 1
            if i == 6:
                if position_letter[k] < len(liste_final[k]):
                    grille[i][j] = liste_final[k][position_letter[k]]
                    position_letter[k] = position_letter[k] + 1
            # 7 #
            j = j + 1
        i = i + 1
    return grille

def fc_grille():
    file = "liste.de.mots.francais.frgut.txt"
    liste = fc_open(file)
    liste_final = fc_create_liste(liste)
    print(liste_final)
    grille = fc_liste_to_grille(liste_final)
    # print grille
    for ligne in grille:
        for cellule in ligne:
            print(cellule + " ", end='')
        print('')
    return grille