#coding=utf-8
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""表示单个外形人的类"""
	def __init__(self, screen, ai_setting):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_setting = ai_setting

		# 加载外形人图像
		self.image = pygame.image.load('image/alien.bmp')
		self.rect = self.image.get_rect()

		# 外形人的初始位置在左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 外形人的精确位置	
		self.x = float(self.rect.x)

	def blitme(self):
		# 在指定位置绘制外形人的图像
		self.screen.blit(self.image, self.rect)
				

		