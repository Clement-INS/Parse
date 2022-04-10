""" Librairies """
import json
import re
import unicodedata
from dataclasses import dataclass


# Représente les données associées à un parti
@dataclass
class Datas:
    """Class representing datas we get from the videos"""
    views: int = 0  # nb vues du parti
    time: float = 0.0  # durées de vidéos sur le parti en heure


def remove_accents(input_str: str) -> str:
    """Enleve les accents d'un string"""
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])


def nb_views(views_field: str) -> int:
    """ Compte le nombre de vues d'une vidéo """
    if isinstance(views_field, str):
        views_split = views_field.split()
        if len(views_split) >= 1:
            indice = views_split[0][-1]
            if views_split[0][:-1].count(',') > 1:
                result = views_split[0][:-1].replace(',', '')
                return int(result)
            if ((not views_split[0][:-1].isspace())
                    and views_split[0][:-1] != ''):
                result = views_split[0][:-1].replace(',', '.')
                if indice == 'K':
                    return int(float(result)*1e3)
                if indice == 'M':
                    return int(float(result)*1e6)
                if indice == 'B':
                    return int(float(result)*1e9)
                return int((result+indice)
                           .replace('.', '')
                           .replace(',', ''))
    return 0


def nb_time(watch_time: str) -> float:
    """
    Converti le string correspondant au temps d'une vidéo en
    un chiffre représentant ce temps en heures
    """
    if isinstance(watch_time, str):
        nb_wtime = watch_time.split(':')
        if len(nb_wtime) == 2:
            result = float(nb_wtime[0])/60.0 + float(nb_wtime[1])/3600.0
            return result
        if len(nb_wtime) == 3:
            result = float(nb_wtime[0]) + float(nb_wtime[1])/60.0
            result += float(nb_wtime[2])/3600.0
            return result
    return 0.0


def get_list_supports():
    """
    Renvoie la liste des noms associés aux candidats
    et leurs supports en majuscule
    """
    with open('candidates_and_supports.json', encoding="utf-8") as json_cas:
        with open('candidats.json', encoding='utf-8') as json_candidats:
            partis_data = {}
            candidates_and_supports = json.load(json_cas)
            candidats = json.load(json_candidats)
            for partie in candidates_and_supports:
                if partie not in partis_data:
                    partis_data[partie] = Datas()
                list_of_cands_supps = []
                for candidate in candidates_and_supports[partie]:
                    names = candidate.split(' ')
                    good_name = []
                    for name in names:
                        if name[-1].isupper():
                            good_name.append(name)
                    list_of_cands_supps.append(' '.join(good_name))
                candidates_and_supports[partie] = list_of_cands_supps
            return (partis_data, candidates_and_supports, candidats)


def sort_video(title, candidats) -> str:
    """
    Indique si le titre d'une vidéo contient le nom
    d'un candidat ou de ses supports
    """
    title = remove_accents(title).upper()
    for name in candidats.keys():
        # pattern = "(?:^|\W)"+name+"(?:$|\W)"
        pattern = r"^((?!gaetan).)*(?:^|\W)" + name + r"(?:$|\W)"
        if re.search(pattern, title, re.UNICODE):
            return candidats[name]
    return ""

def add_parti_data(bdd, name, scenario, video, views, wtime, extract_date):
    """
    Ajoute les données d'une vidéo au parti associé selon le titre de la vidéo:
    """
    # listSupports = getListSupports()
    # title = remove_accents(title)
    # title = title.upper()
    # for partie in listSupports:
    #     for name in listSupports[partie]:
    #         pattern = "(?:^|\W)"+name+"(?:$|\W)"
    #         if re.search(pattern, title, re.UNICODE):
    #             print("url : {} , titre : {}".format(len(url),len(titre)))
    #             # bdd.set.addVideo(partie,filename,views,time,
    #                                pronf,homepos,date, url, titre)
    #             break
    bdd.set.addVideo(
            name,
            scenario,
            video,
            views,
            wtime,
            extract_date
            )
