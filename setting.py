import pygame
import sys

# класс для хранения настроек
class Settings():
	"""docstring for Setting"""
	def __init__(self):
		# параметры экрана
		self.colour = (230, 230, 230)
		self.screen_width = 1200
		self.screen_height = 800	
		# параметры коробля
		self.ship_speed = 1.5

		# параметры пули
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)

		# скорость и перемещение флота
		self.alien_speed = 1
		self.alien_fleet = 1
		self.alien_fleet_drop_speed = 10