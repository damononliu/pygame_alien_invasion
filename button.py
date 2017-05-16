#coding=utf-8
import pygame.font

class Button():
	"""初始化按钮的属性"""
	def __init__(self, screen, msg):
		self.screen = screen
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

	def prep_msg(self, msg):
		"""将msg渲染为图像，并使其在按钮上居中"""
		# render将存储在msg中的文本转换为图像，然后将图像存储在msg_image中，布尔实参指定
		# 开启还是关闭反锯齿功能（反锯齿让文本的边缘更光滑）。再就是文本颜色和背景色
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self):
		# 绘制一个用颜色填充的按钮，再填充文本
		#fill是screen这一surface的函数，用于填充screen上的一个部分，
		#Fill the Surface with a solid color. If no rect argument is 
		#given the entire Surface will be filled. The rect argument 
		#will limit the fill to a specific area. The fill will also 
		#be contained by the Surface clip area.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
