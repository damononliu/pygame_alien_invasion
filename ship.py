#coding=utf-8
import pygame


class Ship():
	"""docstring for Ship"""
	def __init__(self, ai_setting, screen):
		
		self.screen = screen
		self.ai_setting = ai_setting
		self.image = pygame.image.load('image/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom


		self.center1 = float(self.rect.centerx)
		self.center2 = float(self.rect.centery)

		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def update(self):
		# 更新飞船的center值，而不是rect
		# 使飞船不能超出屏幕范围
		if self.move_right and self.rect.right < self.screen_rect.right:
			self.center1 += self.ai_setting.ship_speed_factor
		if self.move_left and self.rect.left > 0:
			self.center1 -= self.ai_setting.ship_speed_factor
		if self.move_up and self.rect.top > 0:
			self.center2 -= self.ai_setting.ship_speed_factor
		if self.move_down and self.rect.bottom < self.screen_rect.bottom:
			self.center2 += self.ai_setting.ship_speed_factor 
		self.rect.centerx = self.center1
		self.rect.centery = self.center2

	def blitme(self):
		self.screen.blit(self.image, self.rect)

