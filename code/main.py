import pygame, sys, time
from settings import *
from sprites import BG

class Game:
  def __init__(self):

    # game setup
    pygame.init()
    self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    self.clock = pygame.time.Clock()

    # sprite groups
    self.all_sprites = pygame.sprite.Group()
    self.collision_sprites = pygame.sprite.Group()

    # scale vector
    bg_height = pygame.image.load('./graphics/environment/background.png').get_height()
    self.scale_factor = WINDOW_HEIGHT/bg_height

    # sprite setup
    BG(self.all_sprites, self.scale_factor)

  def run(self):
    last_time = time.time()
    while True:
      # delta time
      dt = time.time() - last_time
      last_time = time.time()

      # event loop
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      # game logic
      self.all_sprites.draw(self.display_surface)
      pygame.display.update()
      self.clock.tick(FRAMERATE)
  

if __name__ == '__main__':
  game = Game()
  game.run()
