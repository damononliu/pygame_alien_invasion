#coding=utf-8
class Setting():
	"""store all class for setting"""
	def __init__(self):
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		# 子弹设置
		self.bullet_width = 1 
		self.bullet_height = 15
		self.bullet_speed_factor = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 4
		self.alien_factor = 1
		self.fleet_direction = 1
		self.fleet_drop_speed = 10