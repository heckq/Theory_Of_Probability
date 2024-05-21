import matplotlib.pyplot as plt
import numpy as np
import tempfile

def calculate_frequency_polygon(numbers):
    counts, bins = np.histogram(numbers, bins='auto')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    fig, ax = plt.subplots()
    ax.plot(bin_centers, counts, marker='o', linestyle='-', color='b')
    ax.set_title('Частотний Полігон')
    ax.set_xlabel('Числа')
    ax.set_ylabel('Частоти')

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        plt.savefig(temp_file.name)
        plt.close(fig)
        return temp_file.name

def calculate_cumulative_curve(numbers):
    counts, bin_edges = np.histogram(numbers, bins='auto', density=True)
    cdf = np.cumsum(counts)
    cdf = cdf / cdf[-1]

    fig, ax = plt.subplots()
    ax.plot(bin_edges[1:], cdf, marker='o', linestyle='-', color='g')
    ax.set_title('Кумулятивна Крива')
    ax.set_xlabel('Числа')
    ax.set_ylabel('Кумулятивна частота')

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        plt.savefig(temp_file.name)
        plt.close(fig)
        return temp_file.name

def calculate_skewness_graph(numbers):
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    skewness_values = [(x - mean) ** 3 / std_dev ** 3 for x in numbers]

    fig, ax = plt.subplots()
    ax.fill_between(range(len(skewness_values)), skewness_values, color='b', alpha=0.5)
    ax.set_title('Графік Асиметрії')
    ax.set_xlabel('Індекс')
    ax.set_ylabel('Асиметрія')

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        plt.savefig(temp_file.name)
        plt.close(fig)
        return temp_file.name

def calculate_kurtosis_graph(numbers):
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    kurtosis_values = [(x - mean) ** 4 / std_dev ** 4 - 3 for x in numbers]

    fig, ax = plt.subplots()
    ax.fill_between(range(len(kurtosis_values)), kurtosis_values, color='g', alpha=0.5)
    ax.set_title('Графік Ексцесу')
    ax.set_xlabel('Індекс')
    ax.set_ylabel('Ексцес')

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        plt.savefig(temp_file.name)
        plt.close(fig)
        return temp_file.name
