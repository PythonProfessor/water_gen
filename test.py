import pygame
import random
import os
from math import floor, ceil


screen_width = 1400
screen_height = 700
square_size = 20
pygame.init()


class Map:
    def __init__(self, world, names):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption("Map")

        # creates a dictionary of random colors to represent each character
        colors = {}
        for item in names.keys():
            if item not in colors.keys():
                colors[item] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

        # creates a new map with the square sprites in which will form the map
        self.map = []
        self.square_group = pygame.sprite.Group()
        for i in range(len(world)):
            self.map.append([])
            for j in range(len(world[i])):
                square = Square(colors[str(world[i][j])], i, j)
                self.map[i].append(square)
                self.square_group.add(square)
        self.x = 0
        self.y = 0
        self.draw(self.screen)
        pygame.display.flip()

    def draw(self, screen):
        self.square_group.draw(screen)

    def observe(self):
        has_quit = False
        mouse_down = False
        original_x = 0
        original_y = 0
        while not has_quit:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not mouse_down:
                    original_x, original_y = pygame.mouse.get_pos()
                    mouse_down = True

                    # quits if the user clicks outside the map (probably a bad way of doing it)
                    if not 0 <= original_x <= screen_width or not 0 <= original_y <= screen_height:
                        has_quit = True
                        pygame.QUIT()

            # scrolls the map around while the user is holding the mouse down
            while mouse_down:
                final_x, final_y = pygame.mouse.get_pos()
                new_x = (final_x - original_x) / square_size + self.x
                new_y = (final_y - original_y) / square_size + self.y
                original_x = final_x
                original_y = final_y
                if new_x > 0:
                    new_x = 0
                elif -new_x * square_size > len(self.map) * square_size - screen_width:
                    new_x = screen_width / square_size - len(self.map)
                if new_y > 0:
                    new_y = 0
                elif -new_y * square_size > len(self.map[0]) * square_size - screen_height:
                    new_y = screen_height / square_size - len(self.map[0])
                for i in range(floor(-max(self.x, new_x)), ceil(-min(self.x, new_x) + screen_width/square_size)):
                    for j in range(floor(-max(self.y, new_y)), ceil(-min(self.y, new_y) + screen_height/square_size)):
                        self.map[i][j].sync(square_size, new_x*square_size, new_y*square_size)
                self.square_group.draw(self.screen)
                pygame.display.flip()
                self.x = new_x
                self.y = new_y

                # checks whether the user has stopped holding their mouse down
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_down = False

inst = Map(1)
# class for the squares on the map
class Square(pygame.sprite.Sprite):
    def __init__(self, colour, x, y, size=square_size):
        super().__init__()
        self.colour = colour
        self.x = x
        self.y = y
        self.image = pygame.Surface([size, size])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, self.colour, [0, 0, size, size])
        self.sync(size, 0, 0)

    # makes sure the square is in the correct position and is the correct size
    def sync(self, size, map_x, map_y):
        self.rect = self.image.get_rect()
        self.rect.x = self.x * size + map_x
        self.rect.y = self.y * size + map_y
        pygame.transform.scale(self.image, (size, size))

