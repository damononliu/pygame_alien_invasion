#coding=utf-8
import pygame
import sys
from bullet import Bullet


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
			


def update_screen(ai_setting, screen, ship, bullets, alien):
	
	screen.fill(ai_setting.bg_color)
	ship.blitme()
	alien.blitme()
	for bullet in bullets.sprites():
		
		bullet.draw_bullet()
	pygame.display.flip()

def update_bullets(bullets):
	#更新子弹的位置
	bullets.update()
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		#print len(bullets)