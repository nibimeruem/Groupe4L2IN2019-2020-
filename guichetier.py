#coding:utf-8

"""classe mère"""

class agents:
	def __init__(self, nom, ide):
		self.nom = nom
		self.ide = ide

	def travailler(self): #méthode de la classe agents
		print("l'agent {}, matricule {} travaille et il est {}:".format(self.nom, self.ide, self.poste))

"""classe fille"""

class guichetier(agents):  #La classe guichetier herite de la classe agents
	def __init__(self, nom_guichetier, ide_guichetier, poste):
		agents.__init__(self, nom_guichetier, ide_guichetier)
		self.poste = poste


	def retrait(montant, solde = 10000):
		print("Operations de retrait...")
		montant = input("entrer le montant à retitrer:")
		montant = int(montant)
		if montant >= solde:
			print("solde insuffisant !!!")
		else:
			solde -= montant
			print("retrait effectué avec succès !!! Nouveau solde :{}".format(solde))

#pp

g1 = guichetier("DOUNIA DONATIEN", "18A036FS", "Guichetier")

g1.travailler()

g1.retrait()
