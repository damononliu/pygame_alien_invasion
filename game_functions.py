#coding=utf-8
import pygame
import sys
from bullet import Bullet
from alien import Alien


def fire_bullet(bullets, ai_setting, screen, ship):
	if len(bullets) < ai_setting.bullets_allowed:
			new_bullet = Bullet(ship, ai_setting, screen)
			bullets.add(new_bullet)

def check_keydown_events(event, ship, ai_setting, screen, bullets):
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	elif event.key == pygame.K_UP:
		ship.move_up = True
	elif event.key == pygame.K_DOWN:
		ship.move_down = True
	elif event.key == pygame.K_SPACE:

		fire_bullet(bullets, ai_setting, screen, ship)
	elif event.key == pygame.K_q:
		sys.exit()



def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	elif event.key == pygame.K_LEFT:
		ship.move_left = False
	elif event.key == pygame.K_UP:
		ship.move_up = False
	elif event.key == pygame.K_DOWN:
		ship.move_down = False


def check_events(ship, ai_setting, screen, bullets):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, ai_setting, screen, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			


def update_screen(ai_setting, screen, ship, bullets, aliens):
	
	screen.fill(ai_setting.bg_color)
	ship.blitme()

	for bullet in bullets.sprites():
		
		bullet.draw_bullet()
	aliens.draw(screen)
	pygame.display.flip()

def update_bullets(bullets):
	#更新子弹的位置
	bullets.update()
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		#print len(bullets)

def get_numbers_colunm(ai_setting, alien_width):

	available_space_x = ai_setting.screen_width - 2 * alien_width
	number_columes = int(available_space_x / (2 * alien_width))
	return number_columes

def get_numbers_rows(ai_setting, alien_height, ship_height):
	available_space_y = ai_setting.screen_height - 3 * alien_height - ship_height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(screen, ai_setting, aliens, alien_number, row_number):
	alien = Alien(screen, ai_setting)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  
	alien.rect.x = alien.x
	aliens.add(alien)

def create_fleet(screen, ai_setting, aliens, ship):
	alien = Alien(screen, ai_setting)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	number_columes = get_numbers_colunm(ai_setting, alien_width)
	number_rows = get_numbers_rows(ai_setting, alien_height, ship.rect.height)

	for row_number in range(number_rows):
		# 创建第一行外形人
		for alien_number in range(number_columes):
			# 创建一个外形人并将其加入当前行
			create_alien(screen, ai_setting, aliens, alien_number, row_number)