import cv2
import numpy as np


def get_edges_within_depth_range(segmentation_mask, depth_map, min_depth=2.0, max_depth=2.5):

    contours, _ = cv2.findContours(segmentation_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    points_in_depth_range = []

    for contour in contours:
        for point in contour:
            x, y = point[0]

            depth = depth_map[y, x]
            if min_depth <= depth <= max_depth:
                points_in_depth_range.append((x, y, depth))

    return points_in_depth_range


# INSERT REAL DATA EXAMPLES
segmentation_mask = np.zeros((480, 640), dtype=np.uint8)
depth_map = np.zeros((480, 640), dtype=np.float32)

segmentation_mask[100:200, 100:200] = 1
depth_map[100:200, 50:210] = np.random.uniform(2, 2.5, (100, 160))


points_in_depth_range = get_edges_within_depth_range(segmentation_mask, depth_map)


print("Точки на границе объекта с глубиной в диапазоне [2, 2.5] метров:", points_in_depth_range)