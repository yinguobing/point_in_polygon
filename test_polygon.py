import logging
from impl import point_in_polygon

# 将日志文件等级变更为DEBUG可输出运算过程
logging.basicConfig(level=logging.DEBUG)


class TestPointInPolygon:

    def test_point_in_rectangle(self):
        """点在矩形内部"""
        point = [1, 1]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_on_rectangle(self):
        """点在矩形左侧边上"""
        point = [0, 1]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_on_rectangle2(self):
        """点在矩形上侧边上"""
        point = [1, 0]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)
    
    def test_point_on_rectangle3(self):
        """点在矩形下侧边上"""
        point = [1, 2]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_on_vertex(self):
        """点在矩形顶点上"""
        point = [0, 0]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_not_in_rectangle(self):
        """点在矩形外部"""
        point = [5, 5]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon) == False

    def test_point_not_in_rectangle2(self):
        """点在矩形一条边的延长线上"""
        point = [5, 0]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon) == False

    def test_point_not_in_rectangle3(self):
        """点在矩形一条边的延长线上"""
        point = [-5, 0]
        polygon = [[0, 0], [2, 0], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon) == False

    def test_point_in_triangle(self):
        """点在三角形内部"""
        point = [0, -1]
        polygon = [[0, 0], [2, -2], [-2, -2]]
        assert point_in_polygon(point, polygon)

    def test_point_not_in_triangle(self):
        """点在三角形外部"""
        point = [1, -0.5]
        polygon = [[0, 0], [2, -2], [-2, -2]]
        assert point_in_polygon(point, polygon) == False
    
    def test_point_on_vertex_of_triangle(self):
        """点在三角形顶点上"""
        point = [0, 0]
        polygon = [[0, 0], [2, -2], [-2, -2]]
        assert point_in_polygon(point, polygon)

    def test_point_in_polygon(self):
        """点在五边形内部"""
        point = [1, 1]
        polygon = [[0, 0], [2, 0], [3, 1], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_not_in_polygon(self):
        """点五边形外部"""
        point = [-1, -0.5]
        polygon = [[0, 0], [2, 0], [3, 1], [2, 2], [0, 2]]
        assert point_in_polygon(point, polygon) == False

    def test_point_in_non_convex_polygon(self):
        """点在非凸多边形内部"""
        point = [1, 1]
        polygon = [[0, 0], [2, 0], [3, 1], [2, 2], [2, 1], [1, 2], [0, 2]]
        assert point_in_polygon(point, polygon)

    def test_point_not_in_non_convex_polygon(self):
        """点在非凸多边形外部"""
        point = [4, 1]
        polygon = [[0, 0], [2, 0], [3, 1], [2, 2], [2, 1], [1, 2], [0, 2]]
        assert point_in_polygon(point, polygon) == False
