import numpy as np

def process_data(numbers):
    variation_series = sorted(numbers)
    unique, counts = np.unique(variation_series, return_counts=True)
    
    relative_frequencies = counts / len(numbers)
    cumulative_frequencies = np.cumsum(counts)
    relative_cumulative_frequencies = np.cumsum(relative_frequencies)
    
    mode = unique[np.argmax(counts)]
    median = np.median(variation_series)
    mean = np.mean(variation_series)
    variance = np.var(variation_series)
    std_deviation = np.std(variation_series)

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
        'Standard Deviation': std_deviation
    }
    
    return results
