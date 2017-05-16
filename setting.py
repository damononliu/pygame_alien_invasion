#coding=utf-8
class Setting():
	"""store all class for setting"""
	def __init__(self):
		# 屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		# 飞船设置
		self.ship_limit = 3

		# 子弹设置
		self.bullet_width = 2
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 4
		
		# 外星人设置
		self.fleet_drop_speed = 10

		# 游戏加快速率
		self.speed_scale = 1.2

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):

		self.ship_speed_factor = 1.5

		self.bullet_speed_factor = 3

		self.alien_factor = 1
		
		# 1表示向右，-1表示向左
		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speed_scale
		self.bullet_speed_factor *= self.speed_scale
		self.alien_factor *= self.speed_scale