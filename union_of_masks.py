import numpy as np

def union_of_masks(masks: np.array):
    unique_classes, counts = np.unique(masks, axis=0, return_counts=True)
    most_frequent_map = unique_classes[np.argmax(counts, axis=0)]
    
    def most_frequent_in_window(array, window_size):
        pad = window_size // 2
        padded_array = np.pad(array, pad_width=pad, mode='constant', constant_values=-1)
        result = np.empty_like(array)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                window = padded_array[i:i+window_size, j:j+window_size].ravel()
                window = window[window != -1]  # Убираем "пустые" значения
                result[i, j] = np.bincount(window).argmax()
        return result

    smoothed_map = most_frequent_in_window(most_frequent_map, window_size=5)
    return smoothed_map
