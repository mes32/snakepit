
import random

class PositionMap():
    """
    A dictionary of all MapEntities inside the GameLevel
    """

    def __init__(self):
        self.table = dict()
        self.set = set()

    def entity_at(self, position):
        tuple = position.tuple
        if tuple not in self.table:
            return None
        else:
            return self.table[tuple]

    def is_vacant(self, position):
        if self.entity_at(position) == None:
            return True
        else:
            return False

    def insert(self, position, entity):
        self.delete(position)
        tuple = position.tuple
        self.table[tuple] = entity
        self.set.add(entity)

    def delete(self, position):
        tuple = position.tuple
        entity = self.entity_at(position)
        if entity is None:
            return False
        else:
            del self.table[tuple]
            self.set.remove(entity)
            return True

    def list(self):
        return list(self.set)

    def move(self, position_start, position_end):
        if self.is_vacant(position_start) or not self.is_vacant(position_end):
            return False
        else:
            entity = self.entity_at(position_start)
            self.delete(position_start)
            self.insert(position_end, entity)
            return True

    def rand_position(self):
        my_list = self.list()
        index = random.randint(0, len(my_list) - 1)
        return my_list[index].position
