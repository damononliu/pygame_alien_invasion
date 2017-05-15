#coding=utf-8
import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_setting, screen)
	alien = Alien(screen, ai_setting)
	#创建一个用于存储子弹的编组
	bullets = Group()
	while True:
		gf.check_events(ship, ai_setting, screen, bullets)
		#更新飞船的位置
		ship.update()
		gf.update_bullets(bullets)
		#在屏幕上画出子弹和飞船
		gf.update_screen(ai_setting, screen, ship, bullets, alien)
		
	

run_game()