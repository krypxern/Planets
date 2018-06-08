class Body:

	def __init__(self, name="Unknown", mass=0):
		self.name = name
		self.mass = mass

	def step(self):
		print("Test")