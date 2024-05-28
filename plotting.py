import plotly.graph_objects as go
import numpy as np
import os

def calculate_frequency_polygon(numbers):
    counts, bins = np.histogram(numbers, bins='auto')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=bin_centers,
        y=counts,
        mode='lines+markers',
        name='Частотний Полігон',
        line=dict(color='blue')
    ))

    fig.update_layout(
        title='Частотний Полігон',
        xaxis_title='Числа',
        yaxis_title='Частоти'
    )

    file_path = os.path.join(os.getcwd(), 'frequency_polygon.html')
    fig.write_html(file_path)
    return file_path

def calculate_cumulative_curve(numbers):
    counts, bin_edges = np.histogram(numbers, bins='auto', density=True)
    cdf = np.cumsum(counts)
    cdf = cdf / cdf[-1]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=bin_edges[1:],
        y=cdf,
        mode='lines+markers',
        name='Кумулятивна Крива',
        line=dict(color='green')
    ))

    fig.update_layout(
        title='Кумулятивна Крива',
        xaxis_title='Числа',
        yaxis_title='Кумулятивна частота'
    )

    file_path = os.path.join(os.getcwd(), 'cumulative_curve.html')
    fig.write_html(file_path)
    return file_path

def calculate_skewness_graph(numbers):
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    skewness_values = [(x - mean) ** 3 / std_dev ** 3 for x in numbers]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(range(len(skewness_values))),
        y=skewness_values,
        fill='tozeroy',
        name='Графік Асиметрії',
        line=dict(color='blue')
    ))

    fig.update_layout(
        title='Графік Асиметрії',
        xaxis_title='Індекс',
        yaxis_title='Асиметрія'
    )

    file_path = os.path.join(os.getcwd(), 'skewness_graph.html')
    fig.write_html(file_path)
    return file_path

def calculate_kurtosis_graph(numbers):
    mean = np.mean(numbers)
    std_dev = np.std(numbers)
    kurtosis_values = [(x - mean) ** 4 / std_dev ** 4 - 3 for x in numbers]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=list(range(len(kurtosis_values))),
        y=kurtosis_values,
        fill='tozeroy',
        name='Графік Ексцесу',
        line=dict(color='green')
    ))

    fig.update_layout(
        title='Графік Ексцесу',
        xaxis_title='Індекс',
        yaxis_title='Ексцес'
    )

    file_path = os.path.join(os.getcwd(), 'kurtosis_graph.html')
    fig.write_html(file_path)
    return file_path
