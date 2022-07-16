# Point in Polygon
Check if a point is within a polygon, implemented in Python.

There are many algtorithms could resolve this problem. This demo is based on the [Ray Casting algorithm](https://en.wikipedia.org/wiki/Point_in_polygon), which was intruduced as early as 1962 by Shimrat, M..

This algorithm is quite simple: counting how many times a casting ray starting from the point to infinity crosses the polygon, an odd number indicates the point is within the polygon, while an even number means not.
