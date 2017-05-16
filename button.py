import pygame.font

class Button():
	"""初始化按钮的属性"""
	def __init__(self, screen, ):

		self.screen_rect = screen.get_rect()
		# 设置按钮的尺寸和其它属性
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# 创建按钮的rect对象，并使其居中
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# 按钮的标签只需创建一次
		self.prep_msg(msg)

	def prep_msg():
		"""将msg渲染为图像，并使其在按钮上居中"""
		self.