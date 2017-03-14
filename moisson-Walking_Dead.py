# coding: utf-8

# J'ai créé l'univers virtuel en 3 étapes comme vu dans http://jhroy.ca/uqam/edm5240/BeautifulSoup-DocAbregee.pdf

import requests
import csv
from bs4 import BeautifulSoup

# Création de la variable qui nommera mon csv
fich = "walking-dead.csv"

# L'url choisi recense le nombre de téléspectateurs des épisodes de Walking Dead. 
# J'ai choisi d'isoler les données moyennes du nombre de téléspectateurs de chaque saison.
# Il n'y a que les six premières saisons puisque la septième n'est pas encore terminée.
url = "https://en.wikipedia.org/wiki/Template:The_Walking_Dead_ratings"

# Pour être fine et polie
entetes = {
    "User-Agent" : "Camille P.Parent pour un cours de journalisme",
    "From" : "cam.pparent@gmail.com"
}

contenu = requests.get(url, headers=entetes)

page = BeautifulSoup(contenu.text, "html.parser")

# Création de la variable qui inclut ma liste
moyenne = []

# J'ai remarqué en inspectant mon HTML que mes données figurent dans un "td" et qu'en plus, elles sont écrites en italique ("i").
for ligne in page.find_all("td")[1:]:
    # En roulant que print(ligne.find("i")), j'obtenais plusieurs variables None, j'ai donc du passer par-dessus avec try/except.
    # Comme je souhaitais isoler le texte, j'ai ajouté .text puisque sinon j'obtenais mes données entre <i></i>.
    # Et puisque je souhaitais que ma liste soit plus précise, j'ai ajouté un qualicatif "millions de personnes..."
    # J'aurais aimé créer une liste numérotée pour que ce soit encore plus clair quelle est quelle saison, mais je n'y suis pas arrivé.
    # Elles sont toutefois en ordre.
    try:
        print(ligne.find("i").text, "millions de personnes en moyenne ont écouté cette saison de Walking Dead")
    except: 
        pass
    
# Création du fichier .csv
ecrire = open(fich,"a")
truc = csv.writer(ecrire)
truc.writerow(moyenne)
