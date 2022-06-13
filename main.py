import logging
from impl import point_in_polygon

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    point = [1, 0]
    polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
    result = point_in_polygon(point, polygon)
    print(result)
