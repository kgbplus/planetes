#!/usr/bin/env python
# -*- coding: utf-8 -*-

RASPI = False

import os, pygame
from pygame.locals import *
from subprocess import Popen 
from datetime import datetime
if RASPI:
  import RPi.GPIO as GPIO

# GPIO setup
if RASPI:
  GPIO.setmode(GPIO.BCM)
  SWITCH = 21
  GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  RELAY = 18
  GPIO.setup(RELAY, GPIO.OUT)
  GPIO.output(RELAY, False)

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
d = pygame.draw # this will save us writing 'pygame.draw' many times

pygame.display.set_caption("Planetes")

if RASPI:
  bg = pygame.image.load("/home/pi/planetes/planetes_w.jpg")
  video_path = "/home/pi/planetes/video.mp4"
else:
  bg = pygame.image.load("planetes_w.jpg")
  video_path = "video.mp4"

running = True
circle_sel = True
offset = 1.357
planetes_num = 0
planetes_selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
planetes_seq = [0,0,0,0,0]
planetes_seq_win = [5,9,12,8,3]

def write(msg,color):
    if RASPI:
      myfont = pygame.font.Font("/home/pi/planetes/Apriori Light.ttf", 34)
    else:
      myfont = pygame.font.Font("Apriori Light.ttf", 34)
    myfont.set_bold(True)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext

def blink_text1():

  line1 = write("Система требует ввода координат. Обозначьте 5 планет в нужной последовательности".decode("utf-8"),yellow)
  line1_rect = line1.get_rect()
  line1_rect.center = (1920/2,980/2)
  line2 = write("The system requires coordinates. Please, select 5 planets in a right order",yellow)
  line2_rect = line2.get_rect()
  line2_rect.center = (1920/2,1080/2)
  
  blinking = True

  screen.blit(bg,[0,0])
  #d.rect(screen,(0,0,0),(220,320,1500,560))
  rect = pygame.Surface((1550,360),pygame.SRCALPHA,32)
  rect.fill((0,0,255,164))
  screen.blit(rect,(185,360))
  screen.blit(line1,line1_rect)
  screen.blit(line2,line2_rect)
  pygame.display.update()

  while blinking:
    for i in pygame.event.get():
     if i.type == MOUSEBUTTONDOWN:
       blinking = False
       
  screen.fill(black)
  screen.blit(bg,[0,0])
  pygame.display.update()   
  
def blink_text2():
  line1 = write("Координаты неверны, планеты не найдены. Требуется повторный ввод данных".decode("utf-8"),yellow)
  line1_rect = line1.get_rect()
  line1_rect.center = (1920/2,980/2)
  line2 = write("Coordinates are wrong, planets were not found. Re-entry of data is required",yellow)
  line2_rect = line2.get_rect()
  line2_rect.center = (1920/2,1080/2)
  
  blinking = True
  
  screen.blit(bg,[0,0])
  #d.rect(screen,(0,0,0),(220,320,1500,560))
  rect = pygame.Surface((1550,360),pygame.SRCALPHA,32)
  rect.fill((255,0,0,164))
  screen.blit(rect,(185,360))
  screen.blit(line1,line1_rect)
  screen.blit(line2,line2_rect)
  pygame.display.update()

  while blinking:
    for i in pygame.event.get():
     if i.type == MOUSEBUTTONDOWN:
       blinking = False
              
  screen.fill(black)
  screen.blit(bg,[0,0])
  pygame.display.update()   
    
def blink_text3():
  line1 = write("Изменения успешно внесены. Координаты для запуска энергоимпульса получены:".decode("utf-8"),yellow)
  line1_rect = line1.get_rect()
  line1_rect.center = (1920/2,290)
  line2 = write("ДОЛГОТА: TB".decode("utf-8"),yellow)
  line2_rect = line2.get_rect()
  line2_rect.center = (1920/2,340)
  line3 = write("угол Х: 5X".decode("utf-8"),yellow)
  line3_rect = line3.get_rect()
  line3_rect.center = (1920/2,390)
  line4 = write("ШИРОТА: KB".decode("utf-8"),yellow)
  line4_rect = line4.get_rect()
  line4_rect.center = (1920/2,440)
  line5 = write("угол Y: 5E".decode("utf-8"),yellow)
  line5_rect = line5.get_rect()
  line5_rect.center = (1920/2,490)
  
  line6 = write("Changes were successful. Coordinates for launching energy impulse were received",yellow)
  line6_rect = line6.get_rect()
  line6_rect.center = (1920/2,590)
  line7 = write("longitude: TB",yellow)
  line7_rect = line7.get_rect()
  line7_rect.center = (1920/2,640)
  line8 = write("angle Х: 5X",yellow)
  line8_rect = line8.get_rect()
  line8_rect.center = (1920/2,690)
  line9 = write("latitude: KB",yellow)
  line9_rect = line9.get_rect()
  line9_rect.center = (1920/2,740)
  line10 = write("angle Y: 5E",yellow)
  line10_rect = line10.get_rect()
  line10_rect.center = (1920/2,790)
  
  screen.blit(bg,[0,0])
  #d.rect(screen,black,(220,220,1500,660))
  rect = pygame.Surface((1550,640),pygame.SRCALPHA,32)
  rect.fill((0,0,255,164))
  screen.blit(rect,(185,220))
  screen.blit(line1,line1_rect)
  screen.blit(line2,line2_rect)
  screen.blit(line3,line3_rect)
  screen.blit(line4,line4_rect)
  screen.blit(line5,line5_rect)
  screen.blit(line6,line6_rect)
  screen.blit(line7,line7_rect)
  screen.blit(line8,line8_rect)
  screen.blit(line9,line9_rect)
  screen.blit(line10,line10_rect)
  pygame.display.update()
  while (not check_but_state()):
    pygame.time.delay(1000)
  
def exit():
  if (RASPI):
    GPIO.cleanup()
  pygame.quit()

def redraw():
  screen.blit(bg,[0,0])
  for p in range(14):
    if planetes_selected[p]:
      if circle_sel:
        d.ellipse(screen,yellow,(planetes[p][0] - planetes[p][2],planetes[p][1] - planetes[p][2],planetes[p][2]*2*offset,planetes[p][2]*2),10)
        #d.rect(screen,yellow,(planetes[p][0] - planetes[p][2],planetes[p][1] - planetes[p][2],planetes[p][2]*2*offset,planetes[p][2]*2),1) # check_pos zone
      else:
        d.rect(screen,yellow,(planetes[p][0]-planetes[p][2],planetes[p][1]-planetes[p][2],planetes[p][2]*2,planetes[p][2]*2),5)
  pygame.display.update()
  
def restart_planetes():
  global planetes_num
  planetes_num = 0
  for p in range(5):
    planetes_seq[p] = 0
  for p in range(14):
    planetes_selected[p] = 0
  redraw()  
  blink_text1()
  
def check_pos(pos):
  for p in range(14):
    if (((planetes[p][0] - planetes[p][2] < pos[0]) and (planetes[p][0] + planetes[p][2]*(2*offset-1)) > pos[0]) and ((planetes[p][1] - planetes[p][2] < pos[1]) and (planetes[p][1] + planetes[p][2]) > pos[1])):
    #if (((planetes[p][0] - planetes[p][2] < pos[0]) and (planetes[p][0] + planetes[p][2]) > pos[0]) and ((planetes[p][1] - planetes[p][2] < pos[1]) and (planetes[p][1] + planetes[p][2]) > pos[1])):
      return p
      break
  return -1

def timedef_sec(dt):
  return dt.total_seconds()

def check_but_state():
  start_time = datetime.now()
  while (timedef_sec(datetime.now() - start_time) <= 0.1):  # BUTTON CONNECTION WAIT TIME !!!!!!!!!!!!!!!
    if RASPI:
      if (not GPIO.input(SWITCH)):
        return False
      else:
        pygame.time.delay(3000)
  return True  

def check_win():
  if (planetes_seq == planetes_seq_win):
    pygame.time.delay(1500)
    blink_text3()
    if RASPI:
      proc = Popen("exec /usr/bin/omxplayer -o both " + video_path,shell=True)
    #else:
      #proc = Popen("exec /usr/bin/mplayer " + video_path,shell=True)
    if RASPI:
      GPIO.output(RELAY, True)
    pygame.time.delay(60000)
    if RASPI:
      GPIO.output(RELAY, False)
    restart_planetes()
  else:
    pygame.time.delay(1500)
    blink_text2()
    restart_planetes()

# Define some colours
white = (255,255,255); black = (0,0,0); yellow = (255,255,0) 

# coordinates of glass panes
#planetes = [(569, 233, 26),(679, 122, 55),(956, 232, 163),(1268, 276, 71),(1500, 285, 36),(477, 488, 136),(790, 519, 71),(1076, 585, 103),(1457, 649, 91),(479, 874, 95),(724, 820, 62),(932, 909, 86),(1247, 884, 93),(1431, 872, 30)]
planetes = [(438, 233, 26),(572, 122, 55),(902, 232, 163),(1344, 276, 71),(1660, 285, 36),(277, 488, 136),(712, 519, 71),(1079, 585, 103),(1582, 649, 91),(295, 874, 95),(627, 820, 62),(895, 909, 86),(1305, 884, 93),(1571, 875, 30)]

#init screen
screen = pygame.display.set_mode([1920,1080],pygame.FULLSCREEN)
pygame.mouse.set_visible(01)

#let's see the end result
restart_planetes()

while running:
  for i in pygame.event.get():
    if i.type == QUIT or (i.type == KEYDOWN and i.key == K_ESCAPE):
      running = False
      exit()

    elif i.type == MOUSEBUTTONDOWN and i.button == 1:
      planet = check_pos(pygame.mouse.get_pos())  
      if (planet != -1):
        if (not planetes_selected[planet]):
          planetes_num = planetes_num + 1
          planetes_selected[planet] = 1
          planetes_seq[planetes_num-1] = planet
          redraw()
          if planetes_num == 5:
            check_win()

    



