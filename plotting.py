import numpy as np
import matplotlib.pyplot as plt

def calculate_frequency_polygon(data):
    """
    Calculate the frequency polygon.

    Parameters:
        data (list): List of numbers.

    Returns:
        str: Path to the saved image of the frequency polygon.
    """
    # Calculate histogram
    plt.hist(data, bins='auto', edgecolor='black', alpha=0.7)
    plt.title('Frequency Polygon')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Fit a line to the histogram
    hist, bins = np.histogram(data, bins='auto')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    plt.plot(bin_centers, hist, '-')
    
    # Save the plot
    frequency_polygon_path = 'frequency_polygon.png'
    plt.savefig(frequency_polygon_path)
    plt.close()
    
    return frequency_polygon_path

def Plotting():
    pass

def calculate_cumulative_curve(data):
    """
    Calculate the cumulative curve.

    Parameters:
        data (list): List of numbers.

    Returns:
        str: Path to the saved image of the cumulative curve.
    """
    # Calculate cumulative distribution function
    sorted_data = np.sort(data)
    y = np.arange(len(sorted_data)) / float(len(sorted_data))
    
    # Plot cumulative curve
    plt.plot(sorted_data, y, marker='.', linestyle='none')
    plt.title('Cumulative Curve')
    plt.xlabel('Values')
    plt.ylabel('Cumulative Probability')
    plt.grid(True)
    
    # Save the plot
    cumulative_curve_path = 'cumulative_curve.png'
    plt.savefig(cumulative_curve_path)
    plt.close()
    
    return cumulative_curve_path
