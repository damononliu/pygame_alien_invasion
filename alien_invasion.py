#coding=utf-8
import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_functions as gf


def run_game():
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_setting, screen)
	aliens = Group()
	gf.create_fleet(screen, ai_setting, aliens, ship)
	#创建一个用于存储子弹的编组
	bullets = Group()
	while True:
		gf.check_events(ship, ai_setting, screen, bullets)
		#更新飞船的位置
		ship.update()

		gf.update_bullets(bullets, aliens, screen, ai_setting, ship)
		gf.update_aliens(aliens, ai_setting)
		#在屏幕上画出子弹和飞船
		gf.update_screen(ai_setting, screen, ship, bullets, aliens)
		

run_game()