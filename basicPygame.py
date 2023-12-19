# python book by Cyber Ed, page 184

import pygame
import math
import time

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
FPS = 80
PINK = (250, 195, 246)
BLUE = (92, 186, 214)
X_POS = 250
Y_POS = 50
ROE = 150

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
donut_speed = 10


# game
mousePosList = []
finish = False
toggleMouse = True #toggle using keyboard or mouse

while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == LEFT:
				mousePosList.append(pygame.mouse.get_pos())
			if event.button == RIGHT:
				pygame.mixer.music.play()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				mousePosList = []
			elif event.key == pygame.K_KP_ENTER:
				toggleMouse = not toggleMouse
			elif event.key == pygame.K_UP:
				mouse = (mouse[0], mouse[1] - donut_speed)
			elif event.key == pygame.K_DOWN:
				mouse = (mouse[0], mouse[1] + donut_speed)
			elif event.key == pygame.K_RIGHT:
				mouse = (mouse[0] + donut_speed, mouse[1])
			elif event.key == pygame.K_LEFT:
				mouse = (mouse[0] - donut_speed, mouse[1])


	pygame.mouse.set_visible(False)
	screen.blit(image, (0, 0))
	
  if toggleMouse:
		mouse = pygame.mouse.get_pos()
	screen.blit(donut, mouse)

	for pop in mousePosList:
		screen.blit(donut, pop)

	pygame.display.flip()
	clock.tick(FPS)

pygame.quit()
