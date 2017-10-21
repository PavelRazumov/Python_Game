from setting import Settings
from pygame.sprite import Sprite
import sys
import pygame

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self,game_setting, screen, ship):
		
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,0, game_setting.bullet_width,
			game_setting.bullet_height)

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = game_setting.bullet_color
		self.speed = game_setting.bullet_speed

	def update(self):
		self.y -= self.speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)