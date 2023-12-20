# helper file
import pygame

# constants
PINK = (250, 195, 246)
WHITE = (255, 255, 255)
BLUE = (92, 186, 214)
BLACK = (0, 0, 0)
HORIZONTAL_VELOCITY = 4
VERTICAL_VELOCITY = 5
NUM_OF_BALLS = 10
NUM_OF_PLANES = 4

# files
BACKROUND = r"\images\sea.jpg"
MVING_IMG = r"\images\donut.png"
PLANE_FILE = r"\images\plane.png"
SOUND_FILE = r"\sounds\zipzap.wav"


class Ball(pygame.sprite.Sprite):

	def __init__(self, x, y):
		super(Ball, self).__init__()
		self.image = pygame.image.load(MVING_IMG).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.__vx = HORIZONTAL_VELOCITY
		self.__vy = VERTICAL_VELOCITY

	def update_v(self, vx, vy):
		# update velocity
		self.__vx = vx
		self.__vy = vy

	def update_loc(self):
		# update location with current velocity
		self.rect.x += self.__vx
		self.rect.y += self.__vy

	def get_pos(self):
		# get current position
		return self.rect.x, self.rect.y

	def get_v(self):
		# get current velocity
		return self.__vx, self.__vy


class Plane(Ball):
	# like a ball, I changed the photo

	def __init__(self, x, y):
		super(Plane, self).__init__(x, y)
		self.image = pygame.image.load(PLANE_FILE).convert()
		self.image.set_colorkey(WHITE)

