from Body import Body

class Star(Body):

	def __init__(self, name, mass):
		Body.__init__(name,mass)