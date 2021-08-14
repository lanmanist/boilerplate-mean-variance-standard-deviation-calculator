import numpy as np

def calculate_mean(list):
    arr = np.array(list).reshape(3,3)
    mean_list = []
    mean_list.append(arr.mean(axis = 0).tolist())
    mean_list.append(arr.mean(axis = 1).tolist())
    mean_list.append(arr.mean())
    return mean_list

def calculate_variance(list):
    arr = np.array(list).reshape(3,3)
    variance_list = []
    variance_list.append(np.var(arr, axis = 0).tolist())
    variance_list.append(np.var(arr, axis = 1).tolist())
    variance_list.append(np.var(arr))
    return variance_list

def calculate_sd(list):
    arr = np.array(list).reshape(3,3)
    sd_list = []
    sd_list.append(np.std(arr, axis = 0).tolist())
    sd_list.append(np.std(arr, axis = 1).tolist())
    sd_list.append(np.std(arr))
    return sd_list

def calculate_max(list):
    arr = np.array(list).reshape(3,3)
    max_list = []
    max_list.append(arr.max(axis = 0).tolist())
    max_list.append(arr.max(axis = 1).tolist())
    max_list.append(arr.max())
    return max_list

def calculate_min(list):
    arr = np.array(list).reshape(3,3)
    min_list = []
    min_list.append(arr.min(axis = 0).tolist())
    min_list.append(arr.min(axis = 1).tolist())
    min_list.append(arr.min())
    return min_list

def calculate_sum(list):
    arr = np.array(list).reshape(3,3)
    sum_list = []
    sum_list.append(arr.sum(axis = 0).tolist())
    sum_list.append(arr.sum(axis = 1).tolist())
    sum_list.append(arr.sum())
    return sum_list

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        calculations = {
            'mean': calculate_mean(list),
            'variance': calculate_variance(list),
            'standard deviation': calculate_sd(list),
            'max': calculate_max(list),
            'min': calculate_min(list),
            'sum': calculate_sum(list)
        }
    return calculations