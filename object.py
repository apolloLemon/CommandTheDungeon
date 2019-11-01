from game import *
from actor import *
#from object import *

class Object(Entity):
	#Constructor
	nb_cnstrctArg = 1
	def __init__(self, args): #name,pos,dim,health
		super().__init__(args[:-super().nb_cnstrctArg])
		self.vars = args[super().nb_cnstrctArg:]