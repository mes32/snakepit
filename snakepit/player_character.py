import random
import pygame

import map_entity
import map_position

from snake import Snake

class PlayerCharacter(map_entity.MapEntity):
    """
    The player's character in the game.
    """

    def __init__(self, position_lookup, position):
        super(PlayerCharacter, self).__init__(position_lookup, position)
        self.position_lookup = position_lookup
        self.delta_position = map_position.MapPosition(0, 0)

    def copy_stats(self, stats):
        self.current_hp = int(stats.current_hp)
        self.total_hp = int(stats.total_hp)

    def plan_walk(self, x=0, y=0):
        self.delta_position = map_position.MapPosition(x, y)

    def walk(self):
        dx = self.delta_position.x
        dy = self.delta_position.y
        new_position = self.position.delta(dx, dy)
        
        self.move_position(new_position)
        self.delta_position = map_position.MapPosition(0, 0)

    def reset(self):
        self.delta_position = map_position.MapPosition(0, 0)

    def has_died(self):
        if self.current_hp <= 0:
            return True
        else:
            return False

    def hit(self, damage, p_hit):
        if (random.random() <= p_hit):
            self.current_hp = self.current_hp - damage
            if self.current_hp < 0:
                self.current_hp = 0

    def attack(self, enemy):
        damage = 1
        enemy.take_damage(damage)
        # self.current_hp = self.current_hp - 1
        # if self.current_hp < 0:
        #     self.current_hp = 0

    def teleport(self, level):
        terrain = level.terrain_map
        while True:
            position = terrain.rand_position()
            if terrain.is_walkable(position):
                self.move_position(position)
                break

    def pickup(self, item):
        item.consume()
        self.current_hp = self.current_hp + 1
        if self.current_hp > self.total_hp:
            self.current_hp = self.total_hp