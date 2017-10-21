import pygame

class Ship():
	"""docstring for Ship"""
	def __init__(self,game_setting, screen):
		
		self.screen = screen

		self.game_setting = game_setting
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#print(self.rect)
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# сохранение вещественного центра коробля
		self.center = float(self.rect.centerx)

		# движение коробля до упора влево или вправо
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_left and self.rect.left > 0:
			self.center -= self.game_setting.ship_speed
		elif self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_setting.ship_speed
		
		self.rect.centerx = self.center
	# отрисовка корабля 	
	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def return_position(self):
		print('self.rect = ', self.rect, 
				'self.rect.centerx = ', self.rect.centerx,
				'self.rect.bottom', self.rect.bottom)