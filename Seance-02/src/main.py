#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Mettre dans un commentaire le numéro de la question

## Question 1
# Fait

## Question 2
# Fait

## Question 3
# Notre éditeur est VS_Code



## Question 4
# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)



## Question 5
table = pd.DataFrame(contenu)
print(table)



## Question 6
nb_ligne   = len(table)
nb_colonne = len(table.columns)

reponse = "Le tableau contient {} lignes et {} colonnes."
print(reponse.format(nb_ligne, nb_colonne))



## Question 7
# Pour chaque colonne :
#   On extrait le premier élément
#   On regarde son type
#   On le rajoute à la liste
liste_types = []
for nom_colonne in table.columns :
    element = table[nom_colonne][0]
    #print(element, " --- ", type(element))
    if type(element) == str :
        liste_types.append(str)

    elif type(element) == np.float64 :
        liste_types.append(float)

    elif type(element) == np.int64 :
        liste_types.append(int)

    elif type(element) == bool :
        liste_types.append(bool)

    else :
        liste_types.append(None)

print(liste_types)  



## Question 8
print(table.head(0))



## Question 9
inscrits = table["Inscrits"]
print(inscrits)



## Question 10