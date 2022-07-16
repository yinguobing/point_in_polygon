# Point in Polygon

[![Python application](https://github.com/yinguobing/point_in_polygon/actions/workflows/python-app.yml/badge.svg)](https://github.com/yinguobing/point_in_polygon/actions/workflows/python-app.yml)

Check if a point is within a polygon, implemented in Python.

## How to use

Just call the core function `point_in_polygon` like this:

```python3
point = [1, 0]
polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
result = point_in_polygon(point, polygon)
print(result)
```
then it prints:
```python
True
```

## The algorithm

There are many algtorithms could resolve this problem. This demo is based on the [Ray Casting algorithm](https://en.wikipedia.org/wiki/Point_in_polygon), which was intruduced as early as 1962 by Shimrat, M..

This algorithm is quite simple: counting how many times a casting ray starting from the point to infinity crosses the polygon, an odd number indicates the point is within the polygon, while an even number means not.

![Point in polygon](/doc/polygon.jpg)
![Point out of polygon](/doc/polygon1.jpg)

Even though tha algorithm is simple, there are few edge conditions should be considered carefully.

![Point on edge](/doc/point-on-edge.jpg)

![Point on vertice](/doc/point-on-vertice.jpg)

![Wild polygon](/doc/wild-polygon.jpg)

![Lucky rectangle](/doc/lucky-rectangle.jpg)

There are 10+ test cases in the test file `test_polygon.py`. You can add more test cases and run pytest to see if it works.
```bash
python3 -m pytest
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors
Yin Guobing (尹国冰) - [yinguobing](https://yinguobing.com)

![wechat](doc/wechat_logo.png)
