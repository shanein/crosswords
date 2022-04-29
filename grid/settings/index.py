import random
from unicodedata import normalize, combining

# Fonction de recuperation du fichier et exportation des mots dans une liste
def fc_open(file):
    with open(file, "r", encoding='utf-8') as tf:
        lines = tf.read().split('\n')
    return fc_sort_word(lines)

# Fonction pour enlever les accents
def fc_majuscs(ch):
    # suppression des accents qui restent
    chnorm = normalize('NFKD', ch)
    return "".join([c for c in chnorm if not combining(c)])

# Fonction qui trie en fonction du nombre de lettres (limité à 14 lettres maximum pour un mot)
def fc_sort_word(words):
    # retire tous les accents des mots
    for ch in range(len(words)):
        words[ch] = fc_majuscs(words[ch])
    #
    # Melange la liste pour ne pas avoir un ordre alphabetique
    random.shuffle(words)
    #
    i = 0
    liste = [[0 for _ in range(0)] for _ in range(14)]
    while i < 14:
        for word in words:
            if len(word) == i+1:
                liste[i].append(word)
        i = i + 1
    return liste


file = "../../liste.de.mots.francais.frgut.txt"
liste = fc_open(file)

# ordre de recuperation des mots de la grille : 7,3,6,1,4,2,5
# croisements : 7 -> 3,6,1,4
#               1 -> 2
#               4 -> 5

# 7 #
# mot de base choisie aleatoirement #
seven = random.choice(liste[13])
print("7 : " + seven)
letter_seven_to_three = seven[0]
letter_seven_to_six = seven[2]
letter_seven_to_one = seven[6]
letter_seven_to_four = seven[12]
# 7 #

# 3 #
# -> 9 lettres + 5e = 1e du 7
# print(liste[8])
for word in liste[8]:
    if (word[4] == letter_seven_to_three):
        three = word
        print("3 : " + three)
        break
print(letter_seven_to_three)
# 3 #

# 6 #
# -> 5 lettres + 2e = 3e du 7
# print(liste[4])
for word in liste[4]:
    if (word[1] == letter_seven_to_six):
        six = word
        print("6 : " + six)
        break
print(letter_seven_to_six)
# 6 #

# 1 #
# -> 9 lettres + 7e = 7e du 7
# print(liste[8])
for word in liste[8]:
    if (word[6] == letter_seven_to_one):
        one = word
        print("1 : " + one)
        break
print(letter_seven_to_one)
letter_one_to_two = one[1]
# 1 #

# 4 #
# -> 8 lettres + 4e = 13e du 7
# print(liste[7])
for word in liste[7]:
    if (word[3] == letter_seven_to_four):
        four = word
        print("4 : " + four)
        break
print(letter_seven_to_four)
letter_four_to_five = four[6]
# 4 #

# 2 #
# -> 9 lettres + 5e = 2e du 1
# print(liste[8])
for word in liste[8]:
    if (word[4] == letter_one_to_two):
        two = word
        print("2 : " + two)
        break
print(letter_one_to_two)
# 2 #

# 5 #
# -> 3 lettres + 3e = 7e du 4
# print(liste[2])
for word in liste[2]:
    if (word[2] == letter_four_to_five):
        five = word
        print("5 : " + five)
        break
print(letter_four_to_five)
# 5 #

grille = [one, two, three, four, five, six, seven]
print(grille)