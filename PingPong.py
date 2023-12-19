# python book by Cyber Ed, page 176

import pygame
import math
import time

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
FPS = 60
PINK = (250, 195, 246)
BLUE = (92, 186, 214)
IMG = r"C:\Networks\Chapter9\images\sea.jpg"
X_POS = 300
Y_POS = 250
RADIUS = 20


pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hila's Game \n \t\t<< No smile! Only compile ಠ_ಠ >>")
screen.fill(PINK)
clock = pygame.time.Clock()
image = pygame.image.load(IMG)
i = 1


finish = False
while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True

	screen.blit(image, (0, 0))
	pygame.draw.circle(screen, BLUE, [X_POS, Y_POS], RADIUS)
	X_POS += i
	if (X_POS + i) in [700, 0]:
		FPS += 5
		i *= -1

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
