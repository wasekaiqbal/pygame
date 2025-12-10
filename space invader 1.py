import math
import random
import pygame

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_height, screen_width))

background = pygame.image.load('background.png')

pygame.display.set_caption('space invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y
playerx_change = 0
playery_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
no_of_enemy = 6

for _ in range(no_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, screen_width - 64))
    enemyy.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)

bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = 'ready'

score_value = 0
font = pygame.font.Font('freesanbold.tff', 32)
textx = 10
texty = 10

over_font = pygame.font.Font('freesanbold.tff', 64)

def show_score(x,y):
    score = font.render("score:" + str(score_value), True (255, 255, 255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("game over", True (255, 255, 255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy (x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+16,y+10))

def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx-bulletx)**2 + (enemyy - bullety)**2)
    return distance < collision_distance


