import numpy as np

def process_data(numbers):
    variation_series = sorted(numbers)
    unique, counts = np.unique(variation_series, return_counts=True)
    
    relative_frequencies = counts / len(numbers)
    cumulative_frequencies = np.cumsum(counts)
    relative_cumulative_frequencies = np.cumsum(relative_frequencies)
    
    mode = unique[np.argmax(counts)]  # мода
    median = np.median(variation_series)  # медіана
    mean = np.mean(variation_series)  # математичне сподівання
    variance = np.var(variation_series)  # дисперсія 
    std_deviation = np.std(variation_series)  # середнє квадратичне відхилення
    central_moment_second_order = np.mean((variation_series - mean) ** 2) # Центральний момент другого порядку
    skewness = np.mean((variation_series - mean) ** 3) / (std_deviation ** 3) # Асиметрія
    kurtosis = np.mean((variation_series - mean) ** 4) / (std_deviation ** 4) - 3 # Ексцес

    results = {
        'Variation Series': variation_series,
        'Statistical Distribution': dict(zip(unique, counts)),
        'Relative Frequencies': dict(zip(unique, relative_frequencies)),
        'Cumulative Frequencies': dict(zip(unique, cumulative_frequencies)),
        'Relative Cumulative Frequencies': dict(zip(unique, relative_cumulative_frequencies)),
        'Mode': mode,
        'Median': median,
        'Mean': mean,
        'Variance': variance,
        'Standard Deviation': std_deviation,
        'Central Moment (2nd Order)': central_moment_second_order,
        'Skewness': skewness,
        'Kurtosis': kurtosis
    }
    
    return results
