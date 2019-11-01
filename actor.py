from game import *
#from actor import *
from object import *

class Actor(Entity):
	#Constructor
	nb_cnstrctArg = 4
	def __init__(self, args): #name,pos,dim,health
		super().__init__(args[:-super().nb_cnstrctArg])
		self.vars = args[super().nb_cnstrctArg:]
		self.health = args[4]


	#General Stats
	#Combat Interactions
	#Inventory


class Player(Actor):
	#Constructor
	nb_cnstrctArg = 1
	def __init__(self, args): #name,pos,dim,health
		super().__init__(args[:-super().nb_cnstrctArg])
		self.vars = args[super().nb_cnstrctArg:]
	#Player Input
	#Player Stats

class Monster(Actor):
	#Constructor
	nb_cnstrctArg = 1
	def __init__(self, args): #name,pos,dim,health
		super().__init__(args[:-super().nb_cnstrctArg])
		self.vars = args[super().nb_cnstrctArg:]
	#Monster Stats