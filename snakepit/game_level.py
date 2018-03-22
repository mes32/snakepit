import pygame
import random

import terrain_map

from dimensions import Dimensions
from game_level_view import GameLevelView
from heart import Heart
from player_character import PlayerCharacter
from position import Position
from position_map import PositionMap
from snake import Snake
from terrain import Terrain

class GameLevel():
    """
    The current level of the game.
    """

    DIMENSIONS = Dimensions(6, 6)
    terrain_map = terrain_map.TerrainMap(DIMENSIONS)

    def __init__(self, screen, player_stats):
        self.dimensions = self.DIMENSIONS
        
        self.entity_map = PositionMap(self.dimensions)
        self.view = GameLevelView(self, screen)
        self.dim = False

        self._init_terrain()
        self._init_player(player_stats)
        # self._init_enemies()
        self._init_items()

    def _init_terrain(self):
        width = self.dimensions.get_width()
        height = self.dimensions.get_height()

        for x in range(0, width):
            for y in range(0, height):
                walkable = True
                if x == 0 or x == width-1 or y == 0 or y == height-1:
                    walkable = False
                else:
                    walkable = True
                position = Position(self.terrain_map, x, y)
                terrain = Terrain(self.terrain_map, position, walkable)
                self.terrain_map.insert(position, terrain)

    def _init_player(self, player_stats):
        position = self.terrain_map.rand_vacant()
        self.player = PlayerCharacter(self.entity_map, position)
        self.player.copy_stats(player_stats)
        self.entity_map.insert(position, self.player)

    # def _init_enemies(self):
    #     self.enemies = list()

    #     num_enemies = 4
    #     num_enemies = 0
    #     for e in range(0, num_enemies):
    #         position = self.lookup.rand_vacant()
    #         enemy = Snake(self.lookup, position)
    #         self.enemies.append(enemy)

    def _init_items(self):
        terrain_map = self.terrain_map
        entity_map = self.entity_map

        num_items = 3
        for i in range(0, num_items):
            while True:
                position = terrain_map.rand_vacant()
                if entity_map.entity_at(position) is None:
                    break

            item = Heart(entity_map, position)
            entity_map.insert(position, item)

    def update(self):
        self._update_player_character()
        self._update_items()
        # self._update_enemies()

    def _update_items(self):
        entity_list = self.entity_map.list
        for entity in entity_list:
            if type(entity) is Heart and entity.is_consumed == True:
                self.entity_map.remove(entity)

    def _update_player_character(self):
        player = self.player
        position = player.position
        dx = player.delta_position.get_x()
        dy = player.delta_position.get_y()
        new_position = position.delta(dx, dy)

        terrain_map = self.terrain_map
        entity_map = self.entity_map

        # entity = self.lookup.entity_at(new_position)
        # if entity is None:
        #     player.walk()
        # elif type(entity) is Heart:
        #     player.pickup(entity)
        #     player.walk()
        # elif type(entity) is Snake:
        #     player.attack(entity)
        #     player.reset()

        terrain = terrain_map.entity_at(new_position)
        if terrain.is_walkable():
            entity = entity_map.entity_at(new_position)
            if entity is None:
                player.walk()
            elif type(entity) is Heart:
                player.pickup(entity)
                player.walk()

    # def _update_enemies(self):
    #     for enemy in self.enemies:
    #         if enemy.is_dead():
    #             self.enemies.remove(enemy)
    #             self.lookup.remove(enemy)

    #     for enemy in self.enemies:
    #         enemy.wander()

    def set_dim(self, dim):
        self.dim = dim

    def display(self):
        self.view.render()