<<<<<<< HEAD
''' 8x8grid-sense.py
Animation and single frame creation append
for SenseHAT 8x8 LED matrix'''
=======
# bookmarks http://www.one-tab.com/page/Ds6dSsBoSX24cD8OSxqKcA
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
import pygame
import sys
import math
from pygame.locals import *
from led import LED
from buttons import Button
import png # pypng
<<<<<<< HEAD
from sense_hat import SenseHat
=======
from sense_hat import AstroPi
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
import copy, time

saved = True
warning = False
pygame.init()
pygame.font.init()

<<<<<<< HEAD
sh=SenseHat()
screen = pygame.display.set_mode((530, 395sudo ), 0, 32)
=======
ap=AstroPi()
screen = pygame.display.set_mode((500, 530), 0, 32)
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
pygame.display.set_caption('Sense HAT Grid Editor')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 51, 25))
colour = (255,0,0) # Set default colour to red
rotation = 0
frame_number  = 1
fps = 4



def setColourRed():
<<<<<<< HEAD
	global colour
	colour = (255,0,0)

def setColourBlue():
	global colour
	colour = (0,0,255)

def setColourGreen():
	global colour
	colour = (0,255,0)

def setColourPurple():
	global colour
	colour = (102,0,204)

def setColourPink():
	global colour
	colour = (255,0,255)

def setColourYellow():
	global colour
	colour = (255,255,0)

def setColourOrange():
	global colour
	colour = (255,128,0)

def setColourWhite():
	global colour
	colour = (255,255,255)

def setColourCyan():
	global colour
	colour = (0,255,255)

def clearGrid(): # Clears the pygame LED grid and sets all the leds.lit back to False

=======
	global colour 
	colour = (255,0,0)

def setColourBlue():
	global colour 
	colour = (0,0,255)

def setColourGreen():
	global colour 
	colour = (0,255,0)

def setColourPurple():
	global colour 
	colour = (102,0,204)

def setColourPink():
	global colour 
	colour = (255,0,255)

def setColourYellow():
	global colour 
	colour = (255,255,0)

def setColourOrange():
	global colour 
	colour = (255,128,0)

def setColourWhite():
	global colour 
	colour = (255,255,255)

def setColourCyan():
	global colour 
	colour = (0,255,255)

def clearGrid(): # Clears the pygame LED grid and sets all the leds.lit back to False
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	for led in leds:
		led.lit = False

def buildGrid(): # Takes a grid and builds versions for exporting (png and text)

	e = [0,0,0]
	e_png = (0,0,0)

	grid = [
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e,
	e,e,e,e,e,e,e,e
	]
	#png_grid =[]

	png_grid = ['blank','blank','blank','blank','blank','blank','blank','blank']
	for led in leds:
		if led.lit:
			val = led.pos[0] + (8 * led.pos[1])
			#print val
			grid[val] = [led.color[0], led.color[1], led.color[2]]
			if png_grid[led.pos[0]] == 'blank':
				png_grid[led.pos[0]] = (led.color[0], led.color[1], led.color[2])
			else:
				png_grid[led.pos[0]] = png_grid[led.pos[0]] + (led.color[0], led.color[1], led.color[2])
<<<<<<< HEAD
		else:
=======
		else: 
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
			if png_grid[led.pos[0]] == 'blank':
				png_grid[led.pos[0]] = (0,0,0)
			else:
				png_grid[led.pos[0]] = png_grid[led.pos[0]] + (0,0,0)
	return (grid, png_grid)

<<<<<<< HEAD
def piLoad(): # Loads image onto SenseHAT matrix
	grid, grid_png = buildGrid()
	sh.set_pixels(grid)
=======
def piLoad(): # Loads image onto AstroPi matrix
	grid, grid_png = buildGrid()
	ap.set_pixels(grid)
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4

def exportGrid(): # Writes png to file

	global saved
	grid, png_grid = buildGrid()
	FILE=open('image8x8.png','wb')
	w = png.Writer(8,8)
	w.write(FILE,png_grid)
	FILE.close()
	saved = True

def exportCons(): # Writes raw list to console

	grid, png_grid = buildGrid()
	print(grid)


<<<<<<< HEAD
def rotate(): #Rotates image on SenseHAT LED matrix
=======
def rotate(): #Rotates image on AstroPi LED matrix
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	global rotation
	if rotation == 270:
		rotation = 0
	else:
		rotation = rotation + 90
<<<<<<< HEAD
	sh.set_rotation(rotation)
=======
	ap.set_rotation(rotation)
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4



def handleClick():
<<<<<<< HEAD

=======
   
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	global saved
	global warning
	pos = pygame.mouse.get_pos()
	led = findLED(pos, leds)
	if led:
		#print 'led ' + str(led) + ' clicked'
		led.clicked(colour)
		saved = False
	for butt in buttons:
		if butt.rect.collidepoint(pos):
			butt.click()
			#print 'button clicked'
	if warning:
		for butt in buttons_warn:
			if butt.rect.collidepoint(pos):
				butt.click()
<<<<<<< HEAD


def findLED(clicked_pos, leds): # reads leds and checks if clicked position is in one of them

=======
				
 
def findLED(clicked_pos, leds): # reads leds and checks if clicked position is in one of them
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	x = clicked_pos[0]
	y = clicked_pos[1]
	for led in leds:
		if math.hypot(led.pos_x - x, led.pos_y - y) <= led.radius:
			return led
			#print 'hit led'
	return None


def drawEverything():
<<<<<<< HEAD

=======
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	global warning
	screen.blit(background, (0, 0))
	#draw the leds
	for led in leds:
		led.draw()
	for button in buttons:
		button.draw(screen)
	font = pygame.font.Font(None,16)
<<<<<<< HEAD

	frame_text = 'Frame ' + str(frame_number)
	text = font.render(frame_text,1,(255,255,255))
	screen.blit(text, (5,10))
	fps_text = 'Frame rate= ' + str(fps) +' fps'
	text = font.render(fps_text,1,(255,255,255))
	screen.blit(text, (145,10))
	font = pygame.font.Font(None,18)
	export_text = 'Animation'
	text = font.render(export_text,1,(255,255,255))
	screen.blit(text, (445,15))
	export_text = 'Single Frame'
	text = font.render(export_text,1,(255,255,255))
	screen.blit(text, (435,120))
	pygame.draw.circle(screen,colour,(390,345),20,0)
=======
	
	frame_text = 'Frame ' + str(frame_number) 
	text = font.render(frame_text,1,(255,255,255))
	screen.blit(text, (445,370))
	fps_text = 'Frame rate= ' + str(fps) +' fps' 
	text = font.render(fps_text,1,(255,255,255))
	screen.blit(text, (343,440))
	font = pygame.font.Font(None,18)
	export_text = 'Animation'
	text = font.render(export_text,1,(255,255,255))
	screen.blit(text, (30,440))
	export_text = 'Single Frame'
	text = font.render(export_text,1,(255,255,255))
	screen.blit(text, (130,440))
	pygame.draw.circle(screen,colour,(470,345),20,0)
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	#flip the screen
	if warning:
		for button in buttons_warn:
			button.draw(screen)
	pygame.display.flip()

def load_leds_to_animation():

	global frame_number
	global leds
	for saved_led in animation[frame_number]:
				if saved_led.lit:
					for led in leds:
						if led.pos == saved_led.pos:
							led.color = saved_led.color
							led.lit = True

def nextFrame():
<<<<<<< HEAD

=======
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	global frame_number
	global leds
	#print(frame_number)
	animation[frame_number] = copy.deepcopy(leds)
	#clearGrid()
	frame_number+=1
	if frame_number in animation:
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
<<<<<<< HEAD
				led = LED(radius=20,pos=(x, y))
				leds.append(led)
		load_leds_to_animation()


=======
				led = LED(pos=(x, y))
				leds.append(led)
		load_leds_to_animation()
			
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4

def prevFrame():

	global frame_number
	global leds
	#print(frame_number)
	animation[frame_number] = copy.deepcopy(leds)
	clearGrid()
	if frame_number != 1:
		frame_number-=1
	if frame_number in animation:
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
<<<<<<< HEAD
				led = LED(radius=20,pos=(x, y))
=======
				led = LED(pos=(x, y))
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
				leds.append(led)
		load_leds_to_animation()

def delFrame():
	global frame_number
	#print('ani length is ' + str(len(animation)) + ' frame is ' + str(frame_number))
	if len(animation) > 1:
		animation[frame_number] = copy.deepcopy(leds)
		del animation[frame_number]
<<<<<<< HEAD
		prevFrame()
		for shuffle_frame in range(frame_number+1,len(animation)):
			animation[shuffle_frame] = animation[shuffle_frame+1]
		del animation[len(animation)]

=======
		prevFrame()		
		for shuffle_frame in range(frame_number+1,len(animation)):
			animation[shuffle_frame] = animation[shuffle_frame+1]
		del animation[len(animation)]
		
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4


def getLitLEDs():

	points = []
	for led in leds:
		if led.lit:
			points.append(led.pos)
	return points

# Main program body - set up leds and buttons

leds = []
for x in range(0, 8):
	for y in range(0, 8):
<<<<<<< HEAD
		led = LED(radius=20,pos=(x, y))
=======
		led = LED(pos=(x, y))
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
		leds.append(led)
buttons = []
buttons_warn = []
animation={}
#global frame_number

def play():
<<<<<<< HEAD

=======
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	global leds
	global frame_number
	animation[frame_number] = copy.deepcopy(leds)
	#print 'length of ani is ' + str(len(animation))
	for playframe in range(1,(len(animation)+1)):
<<<<<<< HEAD
		#print(playframe)
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
				led = LED(radius=20,pos=(x, y))
=======
		#print(playframe) 
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
				led = LED(pos=(x, y))
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
				leds.append(led)
			for saved_led in animation[playframe]:
				if saved_led.lit:
					for led in leds:
						if led.pos == saved_led.pos:
							led.color = saved_led.color
							led.lit = True
		piLoad()
		time.sleep(1.0/fps)
<<<<<<< HEAD

=======
		
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
def faster():
	global fps
	fps+=1

def slower():
	global fps
	if fps != 1:
		fps-=1

def exportAni():

	global saved
	FILE=open('animation8x8.py','wb')
<<<<<<< HEAD
	FILE.write('from sense_hat import SenseHat\n')
	FILE.write('import time\n')
	FILE.write('sh=SenseHat()\n')
=======
	FILE.write('from sense_hat import AstroPi\n')
	FILE.write('import time\n')
	FILE.write('ap=AstroPi()\n')
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	FILE.write('FRAMES = [\n')
	global leds
	global frame_number
	animation[frame_number] = copy.deepcopy(leds)
	#print 'length of ani is ' + str(len(animation))
	for playframe in range(1,(len(animation)+1)):
<<<<<<< HEAD
		#print(playframe)
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
				led = LED(radius=20,pos=(x, y))
=======
		#print(playframe) 
		leds =[]
		for x in range(0, 8):
			for y in range(0, 8):
				led = LED(pos=(x, y))
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
				leds.append(led)
			for saved_led in animation[playframe]:
				if saved_led.lit:
					for led in leds:
						if led.pos == saved_led.pos:
							led.color = saved_led.color
							led.lit = True
		grid, png_grid = buildGrid()
<<<<<<< HEAD

=======
		
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
		FILE.write(str(grid))
		FILE.write(',\n')
	FILE.write(']\n')
	FILE.write('for x in FRAMES:\n')
<<<<<<< HEAD
	FILE.write('\t sh.set_pixels(x)\n')
=======
	FILE.write('\t ap.set_pixels(x)\n')
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	FILE.write('\t time.sleep('+ str(1.0/fps) + ')\n')
	FILE.close()
	saved = True

def prog_exit():
	print('exit clicked')
	global warning
	warning = False
	clearGrid()
	pygame.quit()
	sys.exit()

def save_it():
	print('save clicked')
	global warning
	exportAni()
	warning = False

<<<<<<< HEAD
def quit():
	global saved
	if saved == False:
		nosave_warn()
	else:
		prog_exit()

=======
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
def importAni():
        global leds
        global frame_number
	with open('animation8x8.py') as ll:
		line_count = sum(1 for _ in ll)
	ll.close()

	#animation = {}
	frame_number = 1
	file = open('animation8x8.py')
	for r in range(4):
		file.readline()

	for frame  in range(line_count-8):
		buff = file.readline()

		load_frame = buff.split('], [')
		counter = 1
		leds =[]
		for f in load_frame:
<<<<<<< HEAD

			if counter == 1:
				f = f[2:]
			elif counter == 64:

				f = f[:-4]

			y = int(counter-1)/8
			x = int(counter-1)%8

			#print(str(counter) + ' ' + f + ' x= ' + str(x) + ' y= ' + str(y))
			led = LED(radius=20,pos=(x, y))
			if f == '0, 0, 0':
				led.lit = False

=======
                        
			if counter == 1:
				f = f[2:]
			elif counter == 64:
                                
				f = f[:-4]
			
			y = int(counter-1)/8
			x = int(counter-1)%8
			
			#print(str(counter) + ' ' + f + ' x= ' + str(x) + ' y= ' + str(y))
			led = LED(pos=(x, y))
			if f == '0, 0, 0':
				led.lit = False
			
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
			else:
				led.lit = True
				f_colours = f.split(',')
				#print(f_colours)
				led.color = [int(f_colours[0]),int(f_colours[1]),int(f_colours[2])]
			leds.append(led)
			counter+=1
		animation[frame_number] = copy.deepcopy(leds)
		frame_number+=1
		counter+=1

	file.close()
	#drawEverything()

<<<<<<< HEAD
exportAniButton = Button('Export to py', action=exportAni,  pos=(425, 45), color=(153,0,0))
buttons.append(exportAniButton)
importAniButton = Button('Import from file', action=importAni,  pos=(425, 80), color=(153,0,0))
buttons.append(importAniButton)

exportConsButton = Button('Export to console', action=exportCons, pos=(425, 150), color=(160,160,160))
buttons.append(exportConsButton)
exportPngButton = Button('Export to PNG', action=exportGrid, pos=(425, 185), color=(160,160,160))
buttons.append(exportPngButton)

RotateButton = Button('Rotate LEDs', action=rotate,  pos=(425, 255), color=(205,255,255))
buttons.append(RotateButton)
clearButton = Button('Clear Grid', action=clearGrid,  pos=(425, 220), color=(204,255,255))
buttons.append(clearButton)

quitButton = Button('Quit', action=quit,  pos=(425, 290), color=(96,96,96))
buttons.append(quitButton)

FasterButton = Button('+', action=faster, size=(45,30), pos=(245, 5), color=(184,138,0))
buttons.append(FasterButton)
SlowerButton = Button('-', action=slower, size=(45,30), pos=(295, 5), color=(184,138,0))
buttons.append(SlowerButton)

PlayButton = Button('Play on LEDs', action=play,  pos=(425, 340), color=(184,138,0))
buttons.append(PlayButton)

RedButton = Button('', action=setColourRed, size=(50,30), pos=(365, 10),hilight=(0, 200, 200),color=(255,0,0))
buttons.append(RedButton)
OrangeButton = Button('', action=setColourOrange, size=(50,30), pos=(365, 45),hilight=(0, 200, 200),color=(255,128,0))
buttons.append(OrangeButton)
YellowButton = Button('', action=setColourYellow, size=(50,30), pos=(365, 80),hilight=(0, 200, 200),color=(255,255,0))
buttons.append(YellowButton)
GreenButton = Button('', action=setColourGreen, size=(50,30), pos=(365, 115),hilight=(0, 200, 200),color=(0,255,0))
buttons.append(GreenButton)
CyanButton = Button('', action=setColourCyan, size=(50,30), pos=(365, 150),hilight=(0, 200, 200),color=(0,255,255))
buttons.append(CyanButton)
BlueButton = Button('', action=setColourBlue, size=(50,30), pos=(365, 185),hilight=(0, 200, 200),color=(0,0,255))
buttons.append(BlueButton)
PurpleButton = Button('', action=setColourPurple, size=(50,30), pos=(365, 220),hilight=(0, 200, 200),color=(102,0,204))
buttons.append(PurpleButton)
PinkButton = Button('', action=setColourPink, size=(50,30), pos=(365, 255),hilight=(0, 200, 200),color=(255,0,255))
buttons.append(PinkButton)
WhiteButton = Button('', action=setColourWhite, size=(50,30), pos=(365, 290),hilight=(0, 200, 200),color=(255,255,255))
buttons.append(WhiteButton)

PrevFrameButton = Button('<-', action=prevFrame, size=(30,30), pos=(55, 5), color=(184,138,0))
buttons.append(PrevFrameButton)
NextFrameButton = Button('->', action=nextFrame, size=(30,30), pos=(95, 5), color=(184,138,0))
buttons.append(NextFrameButton)

DelFrame = Button('Delete', action=delFrame, size=(50,25), pos=(365, 415), color=(184,138,0))
buttons.append(DelFrame)

saveButton = Button('Save', action=save_it, size=(60,50), pos=(150, 250),hilight=(200, 0, 0),color=(255,255,0))
buttons_warn.append(saveButton)
QuitButton = Button('Quit', action=prog_exit, size=(60,50), pos=(260, 250),hilight=(200, 0, 0),color=(255,255,0))
buttons_warn.append(QuitButton)



=======
exportAniButton = Button('Export to py', action=exportAni,  pos=(10, 460), color=(153,0,0))
buttons.append(exportAniButton)
importAniButton = Button('Import from file', action=importAni,  pos=(10, 495), color=(153,0,0))
buttons.append(importAniButton)

exportConsButton = Button('Export to console', action=exportCons, pos=(120, 460), color=(160,160,160))
buttons.append(exportConsButton)
exportPngButton = Button('Export to PNG', action=exportGrid, pos=(120, 495), color=(160,160,160))
buttons.append(exportPngButton)

RotateButton = Button('Rotate LEDs', action=rotate,  pos=(230, 460), color=(205,255,255))
buttons.append(RotateButton)
clearButton = Button('Clear Grid', action=clearGrid,  pos=(230, 495), color=(204,255,255))
buttons.append(clearButton)

FasterButton = Button('+', action=faster, size=(45,25), pos=(340, 460), color=(184,138,0))
buttons.append(FasterButton)
SlowerButton = Button('-', action=slower, size=(45,25), pos=(395, 460), color=(184,138,0))
buttons.append(SlowerButton)

PlayButton = Button('Play on LEDs', action=play,  pos=(340, 495), color=(184,138,0))
buttons.append(PlayButton)

RedButton = Button('', action=setColourRed, size=(50,30), pos=(445, 10),hilight=(0, 200, 200),color=(255,0,0))
buttons.append(RedButton)
OrangeButton = Button('', action=setColourOrange, size=(50,30), pos=(445, 45),hilight=(0, 200, 200),color=(255,128,0))
buttons.append(OrangeButton)
YellowButton = Button('', action=setColourYellow, size=(50,30), pos=(445, 80),hilight=(0, 200, 200),color=(255,255,0))
buttons.append(YellowButton)
GreenButton = Button('', action=setColourGreen, size=(50,30), pos=(445, 115),hilight=(0, 200, 200),color=(0,255,0))
buttons.append(GreenButton)
CyanButton = Button('', action=setColourCyan, size=(50,30), pos=(445, 150),hilight=(0, 200, 200),color=(0,255,255))
buttons.append(CyanButton)
BlueButton = Button('', action=setColourBlue, size=(50,30), pos=(445, 185),hilight=(0, 200, 200),color=(0,0,255))
buttons.append(BlueButton)
PurpleButton = Button('', action=setColourPurple, size=(50,30), pos=(445, 220),hilight=(0, 200, 200),color=(102,0,204))
buttons.append(PurpleButton)
PinkButton = Button('', action=setColourPink, size=(50,30), pos=(445, 255),hilight=(0, 200, 200),color=(255,0,255))
buttons.append(PinkButton)
WhiteButton = Button('', action=setColourWhite, size=(50,30), pos=(445, 290),hilight=(0, 200, 200),color=(255,255,255))
buttons.append(WhiteButton)

PrevFrameButton = Button('<-', action=prevFrame, size=(25,25), pos=(442, 385), color=(184,138,0))
buttons.append(PrevFrameButton)
NextFrameButton = Button('->', action=nextFrame, size=(25,25), pos=(472, 385), color=(184,138,0))
buttons.append(NextFrameButton)

DelFrame = Button('Delete', action=delFrame, size=(50,25), pos=(445, 415), color=(184,138,0))
buttons.append(DelFrame)

saveButton = Button('Save', action=save_it, size=(60,50), pos=(150, 180),hilight=(200, 0, 0),color=(255,255,0))
buttons_warn.append(saveButton)
QuitButton = Button('Quit', action=prog_exit, size=(60,50), pos=(260, 180),hilight=(200, 0, 0),color=(255,255,0))
buttons_warn.append(QuitButton)


>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
def nosave_warn():
	global warning
	warning = True
	font = pygame.font.Font(None,48)
<<<<<<< HEAD
	frame_text = 'Unsaved Frames '

=======
	frame_text = 'Unsaved Frames ' 
	
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
	for d in range(5):
		text = font.render(frame_text,1,(255,0,0))
		screen.blit(text, (100,100))
		pygame.display.flip()
		time.sleep(0.1)
		text = font.render(frame_text,1,(0,255,0))
		screen.blit(text, (100,100))
		pygame.display.flip()
		time.sleep(0.1)
	drawEverything()
# Main prog loop


while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			if saved == False:
				nosave_warn()
			else:
				prog_exit()
<<<<<<< HEAD

=======
		
>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
		if event.type == MOUSEBUTTONDOWN:
			handleClick()

	#update the display
	drawEverything()
<<<<<<< HEAD
=======

>>>>>>> a8b81c9884aac689b3eeddc6da70b1c02a8c61d4
