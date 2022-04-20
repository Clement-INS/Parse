""" Librairies """
import sys
import json
from os import listdir
from os.path import isfile, join, basename, normpath

from bdd import BDD
from parse import sort_video, get_list_supports
from parse import add_parti_data, nb_time, nb_views


# Initialisation de la classe d'accès BDD
bdd = BDD()

# Pour lancer le parseur mettre en paramètre le dossier où se trouvent
# les fichiers json de sortie du crawler exemple : python3 ./parse.py ex.json
foldername = sys.argv[1]
candidats = get_list_supports()

onlyfiles = [f for f in listdir(foldername)
             if isfile(join(foldername, f)) and ".json" in f]

extract_date = basename(normpath(foldername))
print("data from ", extract_date)

for filename in onlyfiles:
    print(f'parsing {filename}...')
    with open(f'./{foldername}/{filename}', encoding='utf-8') as f:
        file = json.load(f)
        for video in file:
            (candidat,support) = sort_video((video['title']), candidats)
            if candidat != "":
                try:
                    wtime = nb_time(video["duration"])
                except ValueError:
                    print("EXCEPT TIME", video["duration"])
                    continue
                try:
                    views = nb_views(video["views"])
                except ValueError:
                    print("EXCEPT VIEWS", video["views"])
                    continue
                add_parti_data(
                        bdd,
                        candidat,
                        support,
                        filename.replace(".json", ""),
                        video,
                        views,
                        wtime,
                        extract_date
                )
    bdd.commit()
