import json,ast,re,unicodedata
import sys
from dataclasses import dataclass

#Pour lancer le parseur mettre en paramètre le fichier json de sortie du crawler exemple : python3 ./parse.py ../output/2022-02-09\ 09:23:42.746607.json

filename = sys.argv[1] 
partisData = {}
partiscandidate = {}

# Représente les données associées à un parti
@dataclass
class Datas:
    """Class representing datas we get from the videos"""
    views: int = 0 #nb vues du parti
    time : float = 0.0 #durées de vidéos sur le parti en heure

# Enleve les accents d'un string
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Convertit le string correspondant aux vues d'une vidéo en un chiffre
def nbViews(views):
    if isinstance(views, str):
        nb_views = views.split()
        if (len(nb_views) >=1):
            indice = nb_views[0][-1]
            if nb_views[0][:-1].count(',') > 1:
                result = nb_views[0][:-1].replace(',','')
                return int(result)
            elif (not nb_views[0][:-1].isspace()) and nb_views[0][:-1] != '':
                result = nb_views[0][:-1].replace(',','.')
                if (indice == 'K'):
                    result = int(float(result)*1e3)
                elif (indice == 'M'):
                    result = int(float(result)*1e6)
                elif (indice == 'B'):
                    result = int(float(result)*1e9)
                else:
                    result = int((result+indice).replace('.','').replace(',',''))
                return result
    return 0

# Converti le string correspondant au temps d'une vidéo en un chiffre représentant ce temps en heures
def nbTime(time):
    if isinstance(time, str):
        nb_time = time.split(':')
        if (len(nb_time) == 2):
            result = float(nb_time[0])/60.0 + float(nb_time[1])/3600.0
            return result
        elif (len(nb_time) == 3):
            result = float(nb_time[0]) + float(nb_time[1])/60.0 + float(nb_time[2])/3600.0
            return result
    return 0.0

# Renvoies la liste des noms associés aux candidats et leurs supports en majuscule
def getListSupports():
    with open('candidates_and_supports.json') as json_file:
        candidatesAndsupports = json.load(json_file)
        for partie in candidatesAndsupports:
            if (partie not in partisData.keys()):
                partisData[partie] = Datas()
            listOfCandsSupps = []
            for candidate in candidatesAndsupports[partie]:
                name = candidate.split(' ')
                goodName = []
                for n in name:
                    if (n[-1].isupper()):
                        goodName.append(n)
                goodName = ' '.join(goodName)
                listOfCandsSupps.append(goodName)
            candidatesAndsupports[partie] = listOfCandsSupps
        return candidatesAndsupports

# Ajoute les données d'une vidéo au parti associé selon le titre de la vidéo:
# addPartisData(listSupports, video["title"], nbViews(video["views"], nbTime["duration"]))
def addPartisData(listSupports, title, views, time, pronf, homepos):
    title = remove_accents(title)
    title = title.upper()
    for partie in listSupports:
        for name in listSupports[partie]:
            pattern = "(?:^|\W)"+name+"(?:$|\W)"
            if re.search(pattern, title, re.UNICODE):
                #AJOUTER DANS LA BASE DE DONNÉE ICI !!!
                break

# Main
with open(filename) as f:
    file = json.load(f)
    listSupports = getListSupports()
    for video in file:
        #print(video.keys())
        #break
        #print(nbViews(video["views"]))
        addPartisData(listSupports, video["title"], nbViews(video["views"]), nbTime(video["duration"]), video["refreshNB"], video["homePosition"])
        #print(video["homePosition"])
        #print("url : ",video["url"])
        # print("views : ",video["views"])
        #print("duration : ",video["duration"])
        #print(nbTime(video["duration"]))
        # print("subscribers : ",video["subscribers"])
        # print("title : ",video["title"])
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        # print("watchTime : ",video["watchTime"])
    #print(partisData)
    #print(partisData['La Republique en marche'].views)