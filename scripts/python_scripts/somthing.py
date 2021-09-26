from Vectors import Vector, Colour
from noises import Perlin, Simplex, colmap
import random
import pygame


class World:
	def __init__(self, 
	size: tuple, 
	noisetype: "class" = Simplex, 
	seed: int = 1234, 
	octaves: int = 7, 
	scale: int = 250, 
	lacunarity: int = 2, 
	persistence: int = 0.5) -> None:

		self.size = size
		self.seed = seed
		self.octaves = octaves
		self.scale = scale
		self.lacunarity = lacunarity
		self.persistence = persistence

		self.noiseinstance = noisetype(
			self.size[0],
			self.size[1], 
			self.seed, 
			self.octaves, 
			self.scale, 
			self.lacunarity, 
			self.persistence)

		self.noise = self.noiseinstance()
		self.colmap = self._genImage()

	def _genImage(self) -> pygame.surface.Surface:
		bytesimage = colmap(self.noiseinstance).tobytes("raw", 'RGB')
		image = pygame.image.fromstring(bytesimage, self.size, 'RGB')
		return image

	def get_at(self, pos: Vector) -> float:
		return self.noise[int(pos[1])][int(pos[0])]


class Plant:
	def __init__(self, 
	pos: Vector, 
	heightrange: tuple, 
	growthrate: float = 0.001, 
	spreadrange: int = 20, 
	colour: Colour = Colour("GREEN"), 
	nutrition: int = 0.5) -> None:

		self.pos = pos
		self.colour = colour
		self.growthrate = growthrate
		self.heightrange = heightrange
		self.nutrition = nutrition

		self.dead = False


		self.spreadrange = spreadrange


	def eat(self):
		self.dead = True

	def spread(self, size) -> 'Plant':
		if random.random() <= self.growthrate:
			newpos = self.pos + Vector(random.randint(-self.spreadrange, self.spreadrange), random.randint(-self.spreadrange, self.spreadrange))
			newpos = Vector(newpos[0] % size[0], newpos[1] % size[1])
			return self.__class__(newpos, self.heightrange, self.growthrate, self.spreadrange, self.colour, self.nutrition)

	def draw(self, screen) -> None:
		pygame.draw.circle(screen, (0, 0, 0), list(self.pos), 2)
		pygame.draw.circle(screen, 
		tuple(self.colour), 
		list(self.pos), 1)

	def __call__(self, things, screen, world) -> bool:
		self.draw(screen)
		if plant:=self.spread(world.size):
			things.append(plant)

	@classmethod
	def genRandom(cls, size: tuple, number: int = 1, heightrange: tuple = (0, 1), growthrate: float = 0.001, spreadrange: int = 20, colour: Colour = Colour("GREEN"), nutrition: int = 50) -> 'Plant':
		randoms = []
		for _ in range(number):
			pos = Vector(
				random.randint(0, size[0]-1), 
				random.randint(0, size[1]-1))

			randoms.append(cls(pos, 
			heightrange, 
			growthrate,
			spreadrange, 
			colour, 
			nutrition))

		if number == 1:
			return randoms[0]
		else:
			return randoms


class Animal:
	def __init__(self,
	 pos: Vector = Vector(0, 0), 
	 vel: Vector = Vector(0, 0), 
	 mass: float = 1, 
	 colour: Colour = Colour("WHITE"), 
	 speed: float = 1, 
	 viewmin: float = 5, 
	 viewmax: float = 10, 
	 littersizerange: list = [1, 4]) -> None:
		self.colour = colour
		self.speed = speed
		self.viewmin = viewmin
		self.viewmax = viewmax

		self.isPregnant = False
		self.timeInfertile = 100
		self.timePreg = 0
		self.pregnancyCooldown=40

		self.maxtimePreg = 0
		self.maxtimeLeftPreg = 0


		self.maxhunger = 1
		self.maxbreeding = 1
		self.hungerincrease = .001
		self.breedingincrease = .001
		self.fear = .5
		self.can_eat = [Plant]
		self.littersize = littersizerange


		self.dead = False

		self.age = 0
		self.hunger = 0
		self.breeding = 0
		self.pos = pos
		self.vel = vel

	def viewrad(self, world):
		# return self.viewmin+((self.viewmax-self.viewmin)/2)
		return self.viewmin+(world.get_at(self.pos))*(self.viewmax-self.viewmin)

	def eat(self):
		self.dead = True

	def checkNearby(self, things, world) -> None:
		possiblemates = []
		possiblefood = []
		predators = []
		food = None
		mate = None
		predator = None
		for i in things:
			if i is self:
				continue
			if (i.pos - self.pos).magnitude < self.viewrad(world):

				if type(i) in self.can_eat:
					possiblefood.append(i)

				elif isinstance(i, self.__class__):
					possiblemates.append(i)

				if hasattr(i, "can_eat"):
					if (self.__class__ in i.can_eat):
						predators.append(i)
# return the closest thing of each type
		if possiblefood:
			food = min(possiblefood, 
			key=lambda x: (x.pos - self.pos).magnitude)

		if possiblemates:
			food = min(possiblemates, 
			key=lambda x: (x.pos - self.pos).magnitude)

		if predators:
			predator = min(predators, 
			key=lambda x: (i.pos - self.pos).magnitude)

		return food, mate, predator

	def checkDead(self):
		dead = False
		if self.hunger > self.maxhunger:
			dead = True
		return dead


	def checkInBounds(self, size):
		self.pos = Vector(self.pos[0] % size[0], self.pos[1] % size[1])

	def checkPreg(self, things):
		if self.timeInfertile>0:
			self.timeInfertile-=1
		else:
			if self.isPregnant:
				self.timePreg+=1
				if self.timePreg >self.maxtimePreg:
                    self.giveBirth(things)
                    print("hi")
					self.timeInfertile = self.pregnancyCooldown

	def update(self,size, things) -> None:
		self.pos += self.vel
		self.checkInBounds(size)

		self.checkPreg(things)

		self.hunger += self.hungerincrease
		self.breeding += self.breedingincrease
		self.breeding = min(self.breeding, self.maxbreeding)

	def draw(self, screen, world) -> None:
		pygame.draw.circle(screen, (0, 0, 0), list(self.pos), self.viewrad(world), width=1)

		pygame.draw.circle(screen, (0, 0, 0), list(self.pos), 2)

		pygame.draw.circle(screen, tuple(self.colour), list(self.pos), 1)

	def giveBirth(self, things):
		littersize = random.randint(self.littersize[0], 
		self.littersize[1])
		for _ in range (littersize):
			things.append(self.__class__(self.pos+Vector(random.randint(-10,10),random.randint(-10,10)),
			self.vel,))


	def __call__(self, animals, screen, world) -> bool:
		if self.checkDead():
			return True
		food, mate, predator = self.checkNearby(animals, world) # returns closest animals
		# issue here where even though the grass is nearby, the animal ignores it because breeding is higher than hunger


		priorities = sorted([
		[food, self.hunger],
		[mate, self.breeding],
		[predator, self.fear]],
		# bug fix here to push things that exist to the highest priority
		key=(lambda x: x[1] if x[0] else 0 ), 
		reverse=True)

		priority = priorities[0][0]

		if priority:
			dist = (priority.pos-self.pos)

			if priority is food:
				self.vel = dist.normalised()*self.speed
				if dist.magnitude<3:
					food.eat() # is in eating disttance of food
					self.hunger =0

			elif priority is mate:
				# fixed ?!
				# cooper pair phenomenon still kinda occurs
				# where one animal wants to mate but the other has 
				if mate.isPregnant or self.isPregnant or self.timeInfertile == 0 or mate.timeInfertile==0:
					self.vel = dist.normalised()*self.speed*-1
				else:
					self.vel = dist.normalised()*self.speed

				if dist.magnitude <3:
					if self.infertile ==0 and not self.isPregnant:
						self.isPregnant = True 

			elif priority is predator:
				self.vel = dist.normalised()*self.speed*-1
		 # is in being eaten disttance
		self.update(world.size, animals)
		self.draw(screen, world)

	@classmethod
	def genRandom(cls, 
	size: tuple, 
	number: int = 1, 
	mass: float = 1, 
	colour: Colour = Colour("WHITE"), 
	speed: float = 0.4, 
	viewmin: float = 5, 
	viewmax: float = 20) -> list:

		randoms = []
		for _ in range(number):
			pos = Vector(random.randint(
				0, size[0]-1), random.randint(0, size[1]-1))
			vel = Vector(random.uniform(-1, 1),
						 random.uniform(-1, 1)).normalised() * speed
			randoms.append(cls(pos, vel, mass, colour, speed, viewmin, viewmax))
		if number == 1:
			return randoms[0]
		else:
			return randoms


class Remains:
	def __init__(self, 
	pos: Vector, 
	colour: Colour = Colour("RED"), 
	nutrition: int = 0.1, 
	numfeeds: int = 1) -> None:

		self.pos = pos
		self.colour = colour
		self.nutrition = nutrition
		self.numfeeds = numfeeds

	def feed(self) -> float:
		self.numfeeds -= 1
		return self.nutrition

	def draw(self, screen) -> None:
		pygame.draw.circle(screen, (0, 0, 0), list(self.pos), 2)
		pygame.draw.circle(screen, tuple(self.colour), list(self.pos), 1)

	def __call__(self, _, screen) -> bool:
		self.draw(screen)
		gone = False if self.numfeeds else True
		return gone


class Simulation:
	def __init__(self, 
	size: tuple, 
	thingtypes: list = [], 
	startofeach: int = 50, 
	maxofeach: int = 100) -> None:

		self.size = size
		self.maxofeach = maxofeach

		self.things = []
		for thing in thingtypes:
			for _ in range(startofeach):
				self.things.append(thing.genRandom(self.size))

		self.world = World(self.size)

	def _initialiseDisplay(self) -> None:
		pygame.init()
		self.display = pygame.display.set_mode(self.size)
		pygame.display.set_caption('EcoSim')
		self.clock = pygame.time.Clock()

	def drawWorld(self) -> None:
		self.display.blit(self.world.colmap, [0, 0])

	def run(self) -> None:
		self._initialiseDisplay()
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == 256:
					running = False
			self.display.fill((0, 0, 0))
			self.drawWorld()
			dead = []
			for thing in self.things:
				thing(self.things, self.display, self.world)
				if thing.dead:
					dead.append(thing)
					self.things.remove(thing)

			'''for thing in dead:
				if isinstance(thing, Animal) or isinstance(thing.__bases__[0], Animal):
					self.things.append(Remains(thing.pos))
				self.things.remove(thing)'''
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	sim = Simulation((500, 500), [Plant, Animal])
	sim.run()
