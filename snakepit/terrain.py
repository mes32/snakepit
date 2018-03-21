import map_entity

class Terrain(map_entity.MapEntity):
    """
    Type of terrain located at a particular tile of PlayingField
    """

    def __init__(self, position_lookup, position):

        # For now any/all terrain objects are non-traversable walls
        super(Terrain, self).__init__(position_lookup, position)
        self.is_walkable = False
