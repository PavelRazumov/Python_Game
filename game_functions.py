import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship

def check_events(game_setting, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True

			elif event.key == pygame.K_LEFT:
				ship.moving_left = True

			elif event.key == pygame.K_SPACE:
				newbullet = Bullet(game_setting, screen, ship)
				bullets.add(newbullet)
			elif event.key == pygame.K_Q:
					sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False

			elif event.key == pygame.K_LEFT:
				ship.moving_left = False

def check_bullet(bullets):
	for bullet in bullets:
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_bullets(bullets, aliens,screen,game_setting,ship):
	collisions = pygame.sprite.pygame.sprite.groupcollide(bullets, aliens, True, True, collided = None)
	if (len(aliens) == 0):
		bullets.empty()
		create_fleets(aliens, screen, game_setting, ship)

def update_screen(ship, aliens,screen, game_setting, bullets):

	screen.fill(game_setting.colour)

	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()# отображение последнего экрана

# создание флота пришельцев
def create_fleets(aliens, screen, game_setting,ship):
	
	alien = Alien(game_setting, screen)
	alien_width = alien.rect.width

	available_space = game_setting.screen_width - (2 * alien_width)

	number_alien = int( available_space / (2 * alien_width))
	print(number_alien)
	number_rows = get_number_rows(game_setting, ship.rect.height, alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_alien):
			alien = Alien(game_setting, screen)
			alien.x = alien_width + 2 * alien_width * alien_number
			
			alien.rect.x = alien.x
			alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
				
			aliens.add(alien)

def get_number_rows(game_setting, ship_height, alien_height):
	available_space_y = (game_setting.screen_height - 
			(3 * alien_height) - ship_height)

	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def check_fleet(game_setting, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet(game_setting,aliens)
			break

# опускать флот и поменять направление
def change_fleet(game_setting, aliens):
	for alien in aliens.sprites():
		alien.rect.y += game_setting.alien_fleet_drop_speed
	game_setting.alien_fleet *= -1


def update_aliens(game_setting, ship, aliens):
	check_fleet(game_setting, aliens)
	# найти любой элемент группы вступившей в коллизию со спрайтом
	if (pygame.sprite.pygame.sprite.spritecollideany(ship, aliens, collided = None)):
		print("ship hit!!!\n")
	aliens.update()