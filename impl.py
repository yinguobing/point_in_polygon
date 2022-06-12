import logging

logger = logging.getLogger(__name__)


def point_in_polygon(point, polygon):
    """判别点是否在多边形内部.

    Args:
        point: 待测试点
        polygon: 待测试多边形

    Returns:
        result: True: 在内部。False: 在外部。
    """
    intersection_count = 0
    num_vertices = len(polygon)
    x, y = point

    for index, vertex in enumerate(polygon):
        x1, y1 = vertex
        x2, y2 = polygon[(index + 1) % num_vertices]

        if point == vertex:
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]端点为起点，+1。")
            intersection_count += 1
            continue

        if y < min(y1, y2):
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]在射线上方，忽略。")
            continue

        if y > max(y1, y2):
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]在射线下方，忽略。")
            continue

        if y1 == y2:
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与射线平行，忽略。")
            continue

        _x = (x1 - x2) / (y1 - y2) * (y - y2) + x2
        if _x > x:
            if y == min(y1, y2):
                logger.debug(
                    f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与射线存在交点[{_x}, {y}]，但是可以忽略。")
                continue
            logger.debug(
                f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与射线存在交点[{_x}, {y}]，+1。")
            intersection_count += 1
        else:
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与射线无交点，忽略。")

    return True if intersection_count % 2 == 1 else False