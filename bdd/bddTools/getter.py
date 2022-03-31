class Get():
	def __init__(self,bdd):
		self.cur = bdd.cur

	# 
	def numberOf(self):
		query = """SELECT COUNT(*) 
				   FROM Video
				   GROUP BY parti,date"""
		self.cur.execute(query)
		return self.cur.fetchall()

	# def numberOf(self,table):
	# 	query = "SELECT COUNT(*) FROM {}".format(table)
	# 	self.cur.execute(query)
	# 	return self.cur.fetchone()[0]

	# def summs(self,carte):
	# 	self.cur.execute("SELECT nom FROM Spell WHERE {} = 1".format(carte))
	# 	res = self.cur.fetchall()
	# 	res = [x[0] for x in res]
	# 	return res

	# def summIcon(self,summoner_name):
	# 	Q_getIcon = "SELECT img FROM Spell WHERE nom = %s"
	# 	self.cur.execute(Q_getIcon,(summoner_name,))
	# 	return self.cur.fetchone()[0]
