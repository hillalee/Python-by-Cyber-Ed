# page 193 in Python by Cyber Ed book
from shapes import Ball
import pygame
import math
import time
import random

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
ROE = 50
FPS = 80

PINK = (250, 195, 246)
BLUE = (92, 186, 214)
NUM_OF_BALLS = 10
DISTANCE = 50
MIN_VEL = -10
MAX_VEL = 10

#mouse controls
LEFT = 1
SCROLL = 2
RIGHT = 3

#photos and audio
IMG = r"C:\Networks\Chapter9\images\sea.jpg"
JEFF = r"C:\Networks\Chapter9\images\donut.png"
SOUND_FILE = r"C:\Networks\Chapter9\sounds\zipzap.wav"


#load game
#audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)

#gui
pygame.display.set_caption("Hila's Game \n \t\t<< No smile! Only compile ಠ_ಠ >>")
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
screen.fill(PINK)
clock = pygame.time.Clock()
image = pygame.image.load(IMG)
donut = pygame.image.load(JEFF)


# game
ballsList = pygame.sprite.Group()
finish = False

while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == LEFT:
				x, y = pygame.mouse.get_pos()
				vx = random.randint(MIN_VEL, MAX_VEL)
				vy = random.randint(MIN_VEL, MAX_VEL)
				ball = Ball(x, y)
				ball.update_v(vx, vy)
				ballsList.add(ball)

	for ball in ballsList:
		vx, vy = ball.get_v()
		x, y = ball.get_pos()
		if (0 >= x + vx) or (x + vx >= WINDOW_WIDTH):
			vx *= -1
			ball.update_v(vx, vy)
		if y + ROE 	<= 0 or y - ROE >= WINDOW_HEIGHT:
			vy *= -1
			ball.update_v(vx, vy)
		ball.update_loc()

	screen.blit(image, (0, 0))
	ballsList.draw(screen)

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
