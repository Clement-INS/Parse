class Manage():
	def __init__(self,bdd):
		self.cur = bdd.cur

	def createTables(self):

		# ----- INFOS

		self.cur.execute("""CREATE TABLE Video (
								ID int PRIMARY KEY AUTO_INCREMENT,
								parti VARCHAR(40), 
								scenario VARCHAR(40),
								vue bigint,
								duree float,
								profondeur int,
								url VARCHAR(70),
								title VARCHAR(200),
								homePosition int,
								date DATE,
							UNIQUE(parti,scenario,vue,duree,profondeur,homePosition,date))""")

	def destroyTable(self,Table):
		self.cur.execute("DROP TABLE {}".format(Table))

	def destroyAllTable(self):
		self.destroyTable("Video")

	def renewTables(self):
		self.destroyAllTable()
		self.createTables()

	def clearTable(self,Table):
		self.cur.execute("TRUNCATE TABLE {}".format(Table))