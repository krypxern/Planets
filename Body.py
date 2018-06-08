class Body:

	def __init__(self, name="Unknown", mass=0, x=0, y=0):
		self.name = name
		self.mass = mass
		self.x = x
		self.y = y

	def step(self):
		print("Test")