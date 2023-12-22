# page 198 in Python by Cyber Ed book, Chapter 11
from shapes import Ball, Plane
import pygame
import math
import time
import random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
ROE = 50
FPS = 80

PINK = (250, 195, 246)
BLUE = (92, 186, 214)

NUM_OF_PLANES = 4
DISTANCE = 50
MAX_VEL = 10

#mouse controls
LEFT = 1
SCROLL = 2
RIGHT = 3

#photos
IMG = r"images\sea.jpg"

#load game
pygame.init()

#gui
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Control \n \t\t<< No smile! Only compile ಠ_ಠ >>")
clock = pygame.time.Clock()
image = pygame.image.load(IMG)
screen.blit(image, (0, 0))


# game
planeList = pygame.sprite.Group()
newPlaneslist = pygame.sprite.Group()

# create planes
for i in range(NUM_OF_PLANES):
	plane = Plane(DISTANCE*i, DISTANCE*i)
	vx = random.randint(-MAX_VEL, MAX_VEL)
	vy = random.randint(-MAX_VEL, MAX_VEL)
	plane.update_v(vx, vy)
	planeList.add(plane)


# game variables
finish = False
collide = False
iterations = 0
orders = 0

while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or iterations == 1000 or collide :
			finish = True

	# find out if planes hit edges
	for plane in planeList:
		vx, vy = plane.get_v()
		x, y = plane.get_pos()
		if (0 >= x + DISTANCE) or (x + DISTANCE >= WINDOW_WIDTH):
			vx *= -1
			plane.update_v(vx, vy)
		if (y + DISTANCE <= 0) or (y + DISTANCE >= WINDOW_HEIGHT):
			vy *= -1
			plane.update_v(vx, vy)
		plane.update_loc()
		

	# find out if planes collide
	newPlaneslist.empty()
	for plane in planeList:
		planesHit = pygame.sprite.spritecollide(plane, planeList, False)
		if len(planesHit) == 1: # only colides with itself
			newPlaneslist.add(plane)
		else:
			collide = True # game over
			finish = True

	# move planes
	for plane in newPlaneslist:
		# get pos and velocity
		x, y = plane.get_pos()
		vx, vy = plane.get_v()

		# check for possible collide
		checkPlane = Plane(x + vx, y + vy)
		dangerHit = pygame.sprite.spritecollide(checkPlane, newPlaneslist, False)
		choices = [vx, vy, (vx, vy)]
		selected = random.choice(choices)

		# randomize vector change
		if len(dangerHit) > 1: # maybe >= ?
			if isinstance(selected, tuple):
				vx *= -1
				vy *= -1
			elif selected == vx:
				vx *= -1
			elif selected == vy:
				vy *= -1
			orders += 1 # point lost
		plane.update_v(vx, vy)


	# update screen with planes
	screen.blit(image, (0, 0))
	planeList.draw(screen)

	pygame.display.flip()
	clock.tick(FPS)

	iterations += 1
	if iterations == 1000:
		finish = True
		win = True

points = iterations * NUM_OF_PLANES - orders
if win:
	print("\t\t YOU WON!")
print("\t\tGAME OVER\n"
	"# iterations made: {}\n"
	  "# orders made: {}\n"
	  "Collide (T/F): {}\n"
	  "Points: {}".format(iterations, orders, collide, points))

pygame.quit()

