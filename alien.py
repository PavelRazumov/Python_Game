from setting import Settings
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self,game_setting,screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.game_setting = game_setting

		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		#print("атрибут get_rect =", self.rect.width)

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if(screen_rect.right <= self.rect.right):
			return True
		
		elif self.rect.left <= 0:
			return True	

	def update(self):
		self.x += (self.game_setting.alien_speed * self.game_setting.alien_fleet)
		self.rect.x = self.x