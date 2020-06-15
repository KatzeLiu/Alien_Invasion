import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    
    # Make agroup to store bulltes in.
    bullets = Group()
    
    # Start the main loop for the game.
    while True:
        
        # Watch for the keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # Get rid of bullets that have disappeared.
        gf.update_bullets(bullets)       
        
        #Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()

            
