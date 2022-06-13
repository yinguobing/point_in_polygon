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
            logger.debug(f"第{index}个顶点[{x1}, {y1}]与测试点重合，在内部。")
            return True

        if y < min(y1, y2):
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]在延长线上方，忽略。")
            continue

        if y > max(y1, y2):
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]在延长线下方，忽略。")
            continue

        if y1 == y2:
            if x > min(x1, x2) and x < max(x1, x2):
                logger.debug(
                    f"点在第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]上，属于内部。")
                return True
            else:
                logger.debug(
                    f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与延长线有重叠，但是点在边外部，忽略。")
            continue

        # 求交点
        _x = (x1 - x2) / (y1 - y2) * (y - y2) + x2
        if _x == x:
            logger.debug(f"点在第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]上，属于内部。")
            return True

        if _x < x:
            logger.debug(f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与延长线无交点，忽略。")
            continue

        # 以下部分：_x > x
        if y == min(y1, y2):
            intersection_count += 1
            logger.debug(
                f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]上端与延长线相交[{_x}, {y}]，+1。")
            continue

        if y == max(y1, y2):
            logger.debug(
                f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]下端与射线存在交点[{_x}, {y}]，但是需要忽略。")
            continue

        intersection_count += 1
        logger.debug(
            f"第{index}条边[[{x1}, {y1}], [{x2}, {y2}]]与射线存在交点[{_x}, {y}]，+1。")

    return True if intersection_count % 2 == 1 else False
