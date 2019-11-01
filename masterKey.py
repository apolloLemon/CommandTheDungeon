class Player:
	#def __init__(self, key, dans):
	#	self.hasKey = key
	#	self.dans = dans

	def __init__(self,dans):
		self.dans = dans
		self.hasKey = False
		self.charisma = 1
		self.health = 1
		self.trapped = True
		
class Salle:
	def __init__(self, name, murs):
		self.name = name
		self.murs = murs

	def listerMurs (self):
		print(self.name+" has:")
		for a in self.murs:
			print(a.nom)

	def get(self,req):
		for a in self.murs:
			if a.nom == req:
				return a
		return 0

	def interactWith(self,req, p):
		i = self.get(req)
		if (i!=0):
			return i.interact(p)
		else:
			print("not found")
class Mur:
	def __init__(self):
		self.nom = "Wall"
		self.text = "This is a wall"

	def interact(self,p):
		print(self.text)
class Porte(Mur):
	doors = 0
	def __init__(self, isOpen):
		self.nom = "Porte"+str(Porte.doors)
		self.isOpen = isOpen
		Porte.doors +=1

	def connect(self, room1, room2):
		self.room1 = room1
		self.room2 = room2

	def interact(self,p):
		if(self.isOpen):
			print("You have entered:")
			if(p.dans == self.room1):
				p.dans = self.room2
				print(self.room2.name)
			else :
				p.dans = self.room1
				print(self.room1.name)
		else:
			if(p.hasKey):
				self.isOpen = True
				print("The door is unlocked")
			else:
				print("Locked Door")

class NamedDoor(Porte):
	def __init__(self,isOpen,name,textL,textO):
		self.isOpen=isOpen
		self.name=name
		self.textL=textL
		self.textO=textO

	def interact(self,p):
		if(self.isOpen):
			print("You have entered:")
			if(p.dans == self.room1):
				p.dans = self.room2
				print(self.room2.name)
			else :
				p.dans = self.room1
				print(self.room1.name)
		else:
			if(p.hasKey):
				self.isOpen = True
				print(self.textO)
			else:
				print(self.textL)

class Meuble(Mur):
	def __init__(self, nom, text):
		self.nom = nom
		self.text = text
class MasterKey(Meuble):
	def __init__(self,nom, text):
		Meuble.__init__(self,nom,text)
		self.hasKey = True

	def interact(self,p):
		print(self.text)
		if(self.hasKey):
			print("There was a key")
			p.hasKey = True
class Stat(Meuble):
	def __init__(self,nom,text,stat,delta):
		Meuble.__init__(self,nom,text)
		self.stat = stat
		self.delta = delta

	def interact(self,p):
		print(self.text)
		if(self.stat=="hp"):
			p.health += self.delta
		elif(self.stat=="chs"):
			p.charisma += self.delta

def MakeDungeon():
	#make all the different objects 
	m = Mur()
	mk = MasterKey("Ornate box","made of bronze")
	ba = Stat("Barrel", "contains wine","chs",1)
	bw = Stat("Crate","contains fruit and bread","hp",1)
	mir = Meuble("Mirror","you see your reflection")
	tap = Meuble("Tapistry","the colors have faded with time")
	torch = Stat("Torch","it burns","hp",-1)
	table = Stat("Table","has food on it","hp",2)

	#make the doors
	EntreOut = Porte(False)
	CaveEntre = Porte(True)
	EntreManger = Porte(True)
	MangerCuisine = Porte(True)
	EntreCuisine = Porte(False)

	#make the rooms and place objects and doors
	Cave = Salle("Cave",[bw,ba,CaveEntre,torch])
	Entre = Salle("Entrance",[mir,CaveEntre,EntreManger,EntreCuisine,EntreOut])
	Cuisine = Salle("Kitchen",[mk,bw,ba,EntreCuisine,MangerCuisine])
	Manger = Salle("Dinning Room",[tap,torch,table,MangerCuisine,EntreManger])
	Out = Salle("Gardens",[EntreOut])

	#connect rooms via doors
	EntreOut.connect(Entre,Out)
	CaveEntre.connect(Entre,Cave)
	EntreManger.connect(Entre,Manger)
	MangerCuisine.connect(Manger,Cuisine)
	EntreCuisine.connect(Cuisine,Entre)

	#put the first room at 0 and the exit at -1
	return [Cave,Entre,Cuisine,Manger,Out]
def Game():
	dungeon = MakeDungeon()

	P1 = Player(dungeon[0])

	turns = 0
	print("Welcome to the dungeon, find the key and escape")
	while(P1.dans.name != dungeon[-1].name):
		turns += 1
		turnChoice = input("\nlook or interact\n")
		if (turnChoice == "look" or turnChoice == "l"):
			P1.dans.listerMurs()
		if(turnChoice == "interact" or turnChoice == "i"):
			target = input("interact with: ")
			target = target.lower().capitalize()
			P1.dans.interactWith(target, P1)
	
	healthstr = " "
	charismastr = " "
	if P1.health < 1 :
		healthstr += "barely "
		charismastr += "but you got out "
	if P1.charisma > 0 :
		charismastr += "in style "

	print("You"+healthstr+"made it outside"+charismastr+"("+str(turns)+" turns)")
Game()