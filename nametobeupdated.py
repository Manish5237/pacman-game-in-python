import pygame
import sys
import copy
from settings import *
from player_class import *
from enemy_class import *

pygame.init()
vec = pygame.math.Vector2


def game_over_draw(self):
    self.screen.fill(BLACK)
    quit_text = "Press the escape button to Quit"
    again_text = "Press Space Bar to Play again"
    self.draw_text("Game Over", self.screen, [WIDTH / 2, 100], 52, RED, "arial", centered=True)
    self.draw_text(again_text, self.screen, [WIDTH // 2, HEIGHT // 2], 36, (190, 190, 190), "arial", centered=True)
    self.draw_text(quit_text, self.screen, [WIDTH // 2, HEIGHT // 1.5], 36, (190, 190, 190), "arial", centered=True)
