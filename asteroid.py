#asteroid file
from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self,screen):
		pygame.draw.circle(screen,"White",self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += (self.velocity * dt)
		return self.position

	def split(self):
		pygame.sprite.Sprite.kill(self)
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		log_event("asteroid_split")
		new_angle = random.uniform(20,50)
		new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
		new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
		new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, new_angle)*1.2
		new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -new_angle)*1.2
