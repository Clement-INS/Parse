class Set():
    def __init__(self, bdd):
        self.cur = bdd.cur

    # def addVideo(self,ugg_id,champ_name):
    # 	Q_Champion = """INSERT INTO Champion (ID,nom) VALUES (%s,%s)
    # 					ON DUPLICATE KEY UPDATE nom=nom"""
    # 	self.cur.execute(Q_Champion,(ugg_id,champ_name))
    def addVideo(self, parti, support, scenario, video, vue, duree, date):
        """ Ajout dans les tables d'infos """
        q_video = """INSERT INTO Video (parti,soutien,scenario,vue,duree,profondeur,
                                        url,title,homePosition,date)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cur.execute(q_video, (parti, support, scenario, vue, duree,
                                   video['refreshNB'], video['url'],
                                   video['title'], video['homePosition'],
                                   date))
