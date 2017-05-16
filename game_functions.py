#coding=utf-8
import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep


def fire_bullet(bullets, ai_setting, screen, ship):
	
	if len(bullets) < ai_setting.bullets_allowed:
			
			new_bullet = Bullet(ship, ai_setting, screen)
			bullets.add(new_bullet)


def check_keydown_events(event, ship, ai_setting, screen, bullets, stats, aliens):
	
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

	elif event.key == pygame.K_p and not stats.game_active:
		start_game(stats, ship, bullets, aliens, screen, ai_setting)


def check_keyup_events(event, ship):
	
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	
	elif event.key == pygame.K_LEFT:
		ship.move_left = False
	
	elif event.key == pygame.K_UP:
		ship.move_up = False
	
	elif event.key == pygame.K_DOWN:
		ship.move_down = False


def check_events(ship, ai_setting, screen, bullets, stats, play_button, aliens):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, ai_setting, screen, bullets, stats, aliens)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y, ship, bullets, aliens, screen, ai_setting)


def check_play_button(stats, play_button, mouse_x, mouse_y, ship, bullets, aliens, screen, ai_setting):
	"""检测鼠标是否点击的是play按钮"""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(stats, ship, bullets, aliens, screen, ai_setting)

def start_game(stats, ship, bullets, aliens, screen, ai_setting):
		# 重置游戏设置
		ai_setting.initialize_dynamic_settings()

		# 隐藏鼠标光标
		pygame.mouse.set_visible(False)

		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True

		# 清空外星人列表和子弹列表
		bullets.empty()
		aliens.empty()

		# 创建一群新的外星人，并将飞船居中
		create_fleet(screen, ai_setting, aliens, ship)
		ship.center_ship()

def update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button):
	
	screen.fill(ai_setting.bg_color)
	
	ship.blitme()

	for bullet in bullets.sprites():	
		bullet.draw_bullet()
	
	aliens.draw(screen)
	
	if not stats.game_active:
		play_button.draw_button()

	pygame.display.flip()


def update_bullets(bullets, aliens, screen, ai_setting, ship):
	
	#更新子弹的位置
	bullets.update()
	
	#删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
		#print len(bullets)
	
	# 让子弹与外星人进行碰撞，进而消灭外星人
	check_bullet_alien_collisions(bullets, aliens, screen, ai_setting, ship)

def check_bullet_alien_collisions(bullets, aliens, screen, ai_setting, ship):
	
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if len(aliens) == 0:
		bullets.empty()
		ai_setting.increase_speed()
		create_fleet(screen, ai_setting, aliens, ship)


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


# 创建一批外星人
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


def check_fleet_edges(aliens, ai_setting):
	
	"""当外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens, ai_setting)
			break
		

def change_fleet_direction(aliens, ai_setting):
	
	"""将整群外星人下移，并改变他们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_setting.fleet_drop_speed
	ai_setting.fleet_direction *= -1


def ship_hit(screen, ai_setting, aliens, ship, stats, bullets):
	
	# 飞船数减1
	if stats.ships_left > 0:
		
		stats.ships_left -= 1
		
		# 清空所有子弹和外星人
		bullets.empty()
		aliens.empty()
	
	
		# 创建一批外星人
		create_fleet(screen, ai_setting, aliens, ship)
		
		# 将飞船居中
		ship.center_ship()

		# 暂停
		sleep(0.5)

	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)	


	


def update_aliens(aliens, ai_setting, ship, screen, stats, bullets):
	
	# 检查是否有外星人到达屏幕边缘
	check_fleet_edges(aliens, ai_setting)
	aliens.update()

	# 检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		#print "Ship hit!!!"
		ship_hit(screen, ai_setting, aliens, ship, stats, bullets)

	check_aliens_bottem(screen, ai_setting, aliens, ship, stats, bullets)


def check_aliens_bottem(screen, ai_setting, aliens, ship, stats, bullets):
	"""检查是否有外星人到达屏幕底端"""	
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 像飞船被撞到一样进行处理
			ship_hit(screen, ai_setting, aliens, ship, stats, bullets)
			break
