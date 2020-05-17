import json
from tiles import Tile
from tile_id import TileID
from spots import LeftSpot, RightSpot, BottomSpot, MiddleSpot, TopSpot


class TileRepo:
    def __init__(self, tile_dict):
        self.__tile_dict = tile_dict

    def get_tile(self, tile_id: TileID) -> Tile:
        return self.__tile_dict[tuple(tile_id)]

    @classmethod
    def get_repo_from_config(cls, filename):
        with open(filename) as config:
            tile_list = json.load(config)["tiles"]
        tile_dictionary = dict()
        for y, row in enumerate(tile_list):
            for x, tile in enumerate(row):
                tile_dictionary[(x+1, y+1)] = Tile.from_config_list(tile)
        return cls(tile_dictionary)


