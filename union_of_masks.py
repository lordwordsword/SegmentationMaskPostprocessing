import numpy as np
import scipy.stats as stats
from scipy import ndimage


def union_of_masks(masks: np.array):
    most_frequent_map = stats.mode(masks, axis=0, keepdims=False).mode
    smoothed_map = ndimage.generic_filter(most_frequent_map, lambda x: np.bincount(x).argmax(), size=5)
    return smoothed_map
