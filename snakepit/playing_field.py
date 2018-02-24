import pygame
import random

from dimensions import Dimensions
from player_character import PlayerCharacter
from playing_field_view import PlayingFieldView
from position import Position
from position_lookup import PositionLookup
from snake import Snake

DIMENSIONS = Dimensions(10, 10)

class PlayingField():
    """
    The current level of the game.
    """

    def __init__(self, player_stats):
        self.dimensions = DIMENSIONS
        self.lookup = PositionLookup(self.dimensions)
        self.view = PlayingFieldView(self)

        self.player_character = PlayerCharacter()
        self.player_character.copy_stats(player_stats)
        self.enemies = list()

        self._init_player_character()
        self._init_enemies()

        # terrain
        # player
        # enemies
        # items
        
        # self._init_terrain()
        # self._init_player()
        # self._init_enemies()
        # self._init_items()
        

    def _init_player_character(self):
        position = self.lookup.rand_vacant()
        self.player_character.set_position(position)
        self.lookup.insert(self.player_character.position, self.player_character)

    def _init_enemies(self):
        num_enemies = 20
        for e in range(0, num_enemies):
            position = self.lookup.rand_vacant()
            enemy = Snake(position)
            self.enemies.append(enemy)
            self.lookup.insert(enemy.position, enemy)

    def update(self):
        self._update_player_character(self.player_character)
        #self._update_enemies()

    def _update_player_character(self, player):
        position = player.position
        # new_position = position.delta_position(player.delta_position)

        # if self._is_wall(new_position):
        #     return
        # else:
        #     player.finalize_walk()

    def _is_wall(self, position):
        # x = position.get_x()
        # y = position.get_y()

        # if x == 0 or x == self.dimensions.get_width() - 1 or y == 0 or y == self.dimensions.get_height() - 1:
        #     return True
        return False

    def display(self, screen):
        self.view.render(screen)