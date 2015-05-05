import pygame
from pygame.locals import *
from pygame import gfxdraw
from random import random
from time import sleep  # To remove

class GUI(object):
    def __init__(self, ecosystem):
        self.size_organism = 4
        self.ecosystem = ecosystem
        size_pixels_x = ecosystem.biotope.size_x * self.size_organism
        size_pixels_y = ecosystem.biotope.size_y * self.size_organism
        pygame.init()
        self.windowSurface = pygame.display.set_mode((size_pixels_x,
                                                      size_pixels_y),
                                                     0, 32)
        pygame.display.set_caption('Ecosystems')
    def draw_ecosystem(self):
        ecosystem = self.ecosystem
        # Draw organisms
        self.windowSurface.fill((0, 0, 0))
        for organism in ecosystem.organisms:

            # Get organism information
            # TODO: access by organism.get_x() or similar
            o_x = organism['status']['coordinates']['x'] * self.size_organism
            o_y = organism['status']['coordinates']['y'] * self.size_organism

            # Draw organism
            # TODO: Define proper color
            if organism['genes']['speed'] == 0.0:
                o_color = (0, 150, 0)
            else:
                o_color = (200, 200, 200)

            px_begin = 1
            px_end = self.size_organism - 1
            pygame.draw.polygon(self.windowSurface,
                                o_color,
                                ((o_x + px_begin, o_y + px_begin),
                                 (o_x + px_end, o_y + px_begin),
                                 (o_x + px_end, o_y + px_end),
                                 (o_x + px_begin, o_y + px_end)))
        pygame.display.update()

    def handle_events(self):
        pass  # Get events and modify Ecosystem accordingly

    def delete(self):
        pygame.quit()

class GUI_functions(object):
    def __init__(self, size_x=500, size_y=500, zoom = 10):
        self.size = (size_x, size_y)
        self.axes_center = (size_x // 2, 3 * size_y // 4)
        self.zoom = zoom
        pygame.init()
        self.windowSurface = pygame.display.set_mode(self.size, 0, 32)
        pygame.display.set_caption('Functions')

    def draw_function(self, f, color = (200, 200, 200)):
        size_x, size_y = self.size
        axes_center_x, axes_center_y = self.axes_center
        zoom = self.zoom
        for x_ in range(size_x):
            x = float(x_ - axes_center_x)/zoom
            y = f(x)
            y_ = axes_center_y - int(y*zoom)
            if (y_ > 0) and (y_ < size_y) and (x_ > 0) and (x_ < size_x):
                gfxdraw.pixel(self.windowSurface, x_, y_, color)
        pygame.display.update()
    
    def handle_events(self):
        pass  # Get events and modify Ecosystem accordingly

    def delete(self):
        pygame.quit()
        
        
        
        
        