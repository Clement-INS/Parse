class Set():
	def __init__(self,bdd):
		self.cur = bdd.cur

	##########  Ajout dans les tables d'infos 

	# def addVideo(self,ugg_id,champ_name):
	# 	Q_Champion = """INSERT INTO Champion (ID,nom) VALUES (%s,%s) 
	# 					ON DUPLICATE KEY UPDATE nom=nom"""
	# 	self.cur.execute(Q_Champion,(ugg_id,champ_name))

	def addVideo(self,parti,scenario,vue,duree,profondeur,homePosition,date,url,title):
		Q_Video = """INSERT INTO Video (parti,scenario,vue,duree,profondeur,homePosition,date,url,title) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		self.cur.execute(Q_Video,(parti,scenario,vue,duree,profondeur,homePosition,date,url,title))