from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

import pygame
import sys

#запуск игры
def run_game():
	pygame.init()
	game_setting = Settings()
	screen = pygame.display.set_mode(
		(game_setting.screen_width, game_setting.screen_height))
	ship = Ship(game_setting, screen)
	#ship.return_position()
	bullets = Group()
	#alien = Alien(game_setting,screen)
	aliens = Group()
	gf.create_fleets(aliens, screen, game_setting,ship)

	while True:
		gf.check_events(game_setting, screen, ship, bullets)# обработка событий
		ship.update()
		# удаление пуль вышедших за экран
		gf.check_bullet(bullets)
		# стрельба(изменение координаты y)
		bullets.update()

		gf.update_screen(ship, aliens,screen, game_setting,bullets)

		gf.update_aliens(game_setting,ship, aliens)
		gf.update_bullets(bullets, aliens, screen, game_setting,ship)
run_game()