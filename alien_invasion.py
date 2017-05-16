#coding=utf-8
import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
	
	pygame.init()
	
	# 创建游戏设置的实例
	ai_setting = Setting()
	
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	
	pygame.display.set_caption("Alien Invasion")

	play_button = Button(screen, "Play")
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_setting)

	ship = Ship(ai_setting, screen)

	aliens = Group()
	
	# 创建一批外星人
	gf.create_fleet(screen, ai_setting, aliens, ship)
	
	#创建一个用于存储子弹的编组
	bullets = Group()
	   
      	while True:
		
			gf.check_events(ship, ai_setting, screen, bullets, stats, play_button, aliens)
		
			if stats.game_active:
				#更新飞船的位置
				ship.update()

				gf.update_bullets(bullets, aliens, screen, ai_setting, ship)
				
				gf.update_aliens(aliens, ai_setting, ship, screen, stats, bullets)
		
			#在屏幕上画出子弹和飞船
			gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button)
		

run_game()