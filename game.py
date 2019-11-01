#from game import *
from actor import *
from object import *

class Game:
	#Constructor
	nb_cnstrctArg = 1
	def __init__(self,args):
		self.vars = args
	#playing field
	#interaction manager

class Board:
	#Constructor
	nb_cnstrctArg = 1
	def __init__(self,args):
		self.vars = args

class Entity:
	#Constructor
	nb_cnstrctArg = 3
	def __init__(self,args):
		self.name = args[0]
		self.pos = args[1]
		self.dim = args[2]
		
		#self.vars = args