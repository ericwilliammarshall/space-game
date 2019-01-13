#e! /usr/local/bin/python3

# eric 3/2014 
# pygame used to move a small ship in a field of stars
# secret for pygame brew install -
# brew install python
# brew install sdl sdl_image sdl_mixer sdl_ttf portmidi 
# brew install --HEAD https://raw.github.com/Homebrew/homebrew-headonly/master/smpeg.rb
# pip install hg+http://bitbucket.org/pygame/pygame

import pygame 
import random

############
### init ###
############

# left - right is x axis
# up - down is y axis
# 0,0 is top left
FRAME_BOTTOM_WALL = 500
FRAME_TOP_WALL = 0
FRAME_RIGHT_WALL = 700 
FRAME_LEFT_WALL = 0
BLOCK_TALL = 50
BLOCK_WIDTH = 50
TORPEDO_TALL=4
TORPEDO_WIDTH=4

# colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)

# stars
class Stars:
	stars=[]
	def __init__(self, number=150):
		for i in range(150):
			x = random.randrange( -FRAME_RIGHT_WALL, FRAME_RIGHT_WALL * 2)
			y = random.randrange( -FRAME_BOTTOM_WALL, FRAME_BOTTOM_WALL * 2)
			self.stars.append([x,y])

	def draw(self, delta_x, delta_y):
		for i in range(len(self.stars)):
			x,y = self.stars[i]
			pygame.draw.circle(screen, white, [x, y], 2)
			self.stars[i] = [ x + delta_x, y + delta_y]
		
# torpedos
class Torpedos:
	def __init__(self):
		pass

	def draw(self):
		pass



# ship
class Ship:
	def __init__(self):
		pass

	def draw(self):
		pass

	def go_up(self):
	 	pass

	def go_down(self):
		pass

	def go_left(self):
		pass

	def go_left(self):
		pass

# pygame setup
pygame.init()
# size is (width, height)
size = (FRAME_RIGHT_WALL,FRAME_BOTTOM_WALL)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("a game")
done = False
clock= pygame.time.Clock()

rect_x = BLOCK_TALL
rect_y = BLOCK_WIDTH
MAX_SPEED=8
rect_delta_x = MAX_SPEED
rect_delta_y = 0
star_delta_x = - rect_delta_x 
star_delta_y = - rect_delta_y
torpedo_delta_x = 0
torpedo_delta_y = 0

the_stars = Stars()

torpedos = []
point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2 + 5]
point2 = [FRAME_RIGHT_WALL//2 , (FRAME_BOTTOM_WALL//2) - 5   ]
point3 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2)]

############
### loop ###
############

while done == False:
	#####  events  #####
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			##### arrow keys #####
			if event.key == pygame.K_LEFT:
				star_delta_x = MAX_SPEED
				star_delta_y = 0 
				torpedo_delta_x = MAX_SPEED 
				# pointing left 
				point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2]
				point2 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2) + 5 ]
				point3 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2) - 5]
			if event.key == pygame.K_RIGHT:
				star_delta_x = -MAX_SPEED 
				star_delta_y = 0 
				torpedo_delta_x = -MAX_SPEED 
				# pointing right
				point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2 + 5]
				point2 = [FRAME_RIGHT_WALL//2 , (FRAME_BOTTOM_WALL//2) - 5   ]
				point3 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2)]
			if event.key == pygame.K_UP:
				star_delta_x = 0
				star_delta_y = MAX_SPEED 
				torpedo_delta_y = MAX_SPEED
    			# pointing up
				point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2]
				point2 = [FRAME_RIGHT_WALL//2 + 5 , (FRAME_BOTTOM_WALL//2 ) + 20]
				point3 = [FRAME_RIGHT_WALL//2 - 5 , (FRAME_BOTTOM_WALL//2) + 20]
			if event.key == pygame.K_DOWN:
				star_delta_x = 0
				star_delta_y = -MAX_SPEED
				torpedo_delta_y = -MAX_SPEED 
				# pointing down
				point1 = [FRAME_RIGHT_WALL//2  ,FRAME_BOTTOM_WALL//2  + 20]
				point2 = [FRAME_RIGHT_WALL//2 + 5 , (FRAME_BOTTOM_WALL//2)    ]
				point3 = [FRAME_RIGHT_WALL//2 - 5  , (FRAME_BOTTOM_WALL//2)]
			##### space key #####
			# torpedo
			if event.key == pygame.K_SPACE:
				torpedos.append([FRAME_RIGHT_WALL//2 + 2, FRAME_BOTTOM_WALL//2 + 2 ,-star_delta_x*2,-star_delta_y*2])  
			##### w key #####
			## 'warp'
			#if event.key == pygame.K_SPACE:
			#	star_delta_x *= 2 
			#	star_delta_y *= 2
				



	##### graphics #####
	screen.fill(black)		

	# stars
	#for i in range(len(stars)):
	#	x,y = stars[i]
	#	pygame.draw.circle(screen, white, [x, y], 2)
	#	stars[i] = [ x + star_delta_x, y + star_delta_y]
	#print("star0 ", stars[0])

	the_stars.draw(star_delta_x, star_delta_y)

	for i in range(len(torpedos)):
		#print(torpedos[i])
		x = torpedos[i][0]
		y = torpedos[i][1]
		pygame.draw.circle(screen, red, [ x, y ], 2)
		# change position
		torpedos[i][0] += torpedos[i][2]
		torpedos[i][1] += torpedos[i][3]
	
	#TORPEDO_TALL=4
	#TORPEDO_WIDTH=4
		
		
	# blue box
	#pygame.draw.rect(screen, blue, [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2 ,50,50] )

	# blue triangle
    # pointing up
#	point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2]
#	point2 = [FRAME_RIGHT_WALL//2 + 5 , (FRAME_BOTTOM_WALL//2 ) + 20]
#	point3 = [FRAME_RIGHT_WALL//2 - 5 , (FRAME_BOTTOM_WALL//2) + 20]

	# pointing left 
#	point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2]
#	point2 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2) + 5 ]
#	point3 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2) - 5]

	# pointing right
#	point1 = [FRAME_RIGHT_WALL//2 ,FRAME_BOTTOM_WALL//2 + 5]
#	point2 = [FRAME_RIGHT_WALL//2 , (FRAME_BOTTOM_WALL//2) - 5   ]
#	point3 = [FRAME_RIGHT_WALL//2 + 20 , (FRAME_BOTTOM_WALL//2)]

	# pointing down
#	point1 = [FRAME_RIGHT_WALL//2  ,FRAME_BOTTOM_WALL//2  + 20]
#	point2 = [FRAME_RIGHT_WALL//2 + 5 , (FRAME_BOTTOM_WALL//2)    ]
#	point3 = [FRAME_RIGHT_WALL//2 - 5  , (FRAME_BOTTOM_WALL//2)]

	# (across, vert)
	# below is a triangle pointing up
	#top = ( 100,90)
	#bottom1 = ( 105,105)
	#bottom2 = (95,105)
	pygame.draw.polygon(screen, blue, [point1,  point2, point3 ] )

	# red box
#	pygame.draw.rect(screen, red, [rect_y,rect_x,50,50] )

#	rect_x += rect_delta_x
#	rect_y += rect_delta_y
	#print("x: ", rect_x, "y: ", rect_y)

	# bounce
#	if rect_x > ( FRAME_BOTTOM_WALL - BLOCK_TALL ) :
#		rect_delta_x = rect_delta_x * -1
#		star_delta_y = star_delta_y * -1
#		print(" bottom ")
#	if rect_x < ( FRAME_TOP_WALL ):
#		rect_delta_x = rect_delta_x * -1
#		star_delta_y = star_delta_y * -1
#		print(" top ")
#
#	if rect_y > ( FRAME_RIGHT_WALL - BLOCK_TALL ) :
#		rect_delta_y = rect_delta_y * -1
#		star_delta_x = star_delta_x * -1
#		print(" right ")
#	if rect_y < ( FRAME_LEFT_WALL):
#		rect_delta_y = rect_delta_y * -1
#		star_delta_x = star_delta_x * -1
#		print(" left ")
#
	pygame.display.flip()
	clock.tick(20)
	

pygame.quit()	
