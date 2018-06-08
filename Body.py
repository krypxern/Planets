import math

def dist(x1, y1, x2, y2):
	return sqrt((x1 - x2)^2 + (y1 - y2)^2)

class Body:

	G = 6.67e-11 #Gravitational Constant

	vx = 0;
	vy = 0;

	Fx = 0;
	Fy = 0;

	def __init__(self, name="Unknown", mass=0, x=0, y=0):
		self.name = name
		self.mass = mass
		self.x = x
		self.y = y

	#Calculates the force of attraction to another planet and adds it to the velocity vector.
	def att(self, oth: "Body"):
		r = dist(self.x, self.y, x, y)
		F = G * self.mass * oth.mass / r^2

		self.Fx = (x2 - x1) / d * F
		self.Fy = (y2 - y1) / d * F

		return F

	def step(self, dt = 0):
		if dt == 0:
			return
		
		ax = Fx / mass
		ay = Fx / mass

		vx += ax * dt
		vy += ay * dt

		x += vx * dt
		y += vy * dt

		Fx = 0
		Fy = 0