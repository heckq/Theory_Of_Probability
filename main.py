import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QTabWidget, QFileDialog
from PyQt5.QtGui import QColor, QPalette, QPixmap  
from PyQt5.QtCore import Qt 
from data_processing import process_data  
from plotting import calculate_frequency_polygon, calculate_cumulative_curve, calculate_skewness_graph, calculate_kurtosis_graph
import cgitb
import codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Statistics Calculator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout() 
        self.central_widget.setLayout(self.layout)

        input_container_layout = QVBoxLayout()  
        self.input_label = QLabel("Введіть числа (розділені пробілами):")
        self.input_field = QLineEdit()
        self.calculate_button = QPushButton("Розрахувати")
        self.calculate_button.clicked.connect(lambda: self.calculate_callback())
        
        self.load_button = QPushButton("Завантажити з файлу")
        self.load_button.clicked.connect(self.load_file)

        input_container_layout.addWidget(self.input_label)
        input_container_layout.addWidget(self.input_field)
        input_container_layout.addWidget(self.calculate_button)
        input_container_layout.addWidget(self.load_button)

        self.layout.addLayout(input_container_layout)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.tab_statistics = QWidget()
        self.tab_graphs = QWidget()
        self.tab_widget.addTab(self.tab_statistics, "Статистика")
        self.tab_widget.addTab(self.tab_graphs, "Графіки")

        self.layout_statistics = QVBoxLayout()
        self.layout_graphs = QVBoxLayout()
        self.tab_statistics.setLayout(self.layout_statistics)
        self.tab_graphs.setLayout(self.layout_graphs)

        tables_container = QWidget()
        tables_layout = QGridLayout(tables_container)
        self.tables = []
        for i, title in enumerate(["Варіаційний ряд", "Статистичний розподіл", "Відносні частоти", "Кумулятивні частоти", "Відносні кумулятивні частоти"]):
            table = QTableWidget()
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(["Статистика", "Значення"])
            self.tables.append(table)
            tables_layout.addWidget(QLabel(f"<b>{title}</b>"), 0, i)
            tables_layout.addWidget(table, 1, i)

        self.layout_statistics.addWidget(tables_container)

        self.mode_label = QLabel()
        self.median_label = QLabel()
        self.mean_label = QLabel()
        self.variance_label = QLabel()
        self.std_deviation_label = QLabel()

        self.layout_statistics.addWidget(self.mode_label)
        self.layout_statistics.addWidget(self.median_label)
        self.layout_statistics.addWidget(self.mean_label)
        self.layout_statistics.addWidget(self.variance_label)
        self.layout_statistics.addWidget(self.std_deviation_label)

        self.graphs_tab_widget = QTabWidget()
        self.layout_graphs.addWidget(self.graphs_tab_widget)

        self.tab_frequency_polygon = QWidget()
        self.tab_cumulative_curve = QWidget()
        self.tab_skewness = QWidget()
        self.tab_kurtosis = QWidget()
        self.graphs_tab_widget.addTab(self.tab_frequency_polygon, "Частотний Полігон")
        self.graphs_tab_widget.addTab(self.tab_cumulative_curve, "Кумулятивна Крива")
        self.graphs_tab_widget.addTab(self.tab_skewness, "Графік Асиметрії")
        self.graphs_tab_widget.addTab(self.tab_kurtosis, "Графік Ексцесу")

        self.layout_frequency_polygon = QVBoxLayout()
        self.layout_cumulative_curve = QVBoxLayout()
        self.layout_skewness = QVBoxLayout()
        self.layout_kurtosis = QVBoxLayout()
        self.tab_frequency_polygon.setLayout(self.layout_frequency_polygon)
        self.tab_cumulative_curve.setLayout(self.layout_cumulative_curve)
        self.tab_skewness.setLayout(self.layout_skewness)
        self.tab_kurtosis.setLayout(self.layout_kurtosis)

        self.label_frequency_polygon = QLabel("Частотний Полігон буде показано тут")
        self.label_cumulative_curve = QLabel("Кумулятивна Крива буде показана тут")
        self.label_skewness = QLabel("Графік Асиметрії буде показаний тут")
        self.label_kurtosis = QLabel("Графік Ексцесу буде показаний тут")
        self.layout_frequency_polygon.addWidget(self.label_frequency_polygon)
        self.layout_cumulative_curve.addWidget(self.label_cumulative_curve)
        self.layout_skewness.addWidget(self.label_skewness)
        self.layout_kurtosis.addWidget(self.label_kurtosis)

    def load_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Виберіть файл з даними", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = file.read()
                self.input_field.setText(data.strip())

    def calculate_callback(self):
        data = self.input_field.text()
        numbers = list(map(float, data.split()))

        results = process_data(numbers)

        for table, (title, values) in zip(self.tables, results.items()):
            if isinstance(values, dict):
                table.setRowCount(len(values))
                for row, (statistic, value) in enumerate(values.items()):
                    table.setItem(row, 0, QTableWidgetItem(str(statistic)))
                    item = QTableWidgetItem("{:.3f}".format(value)) 
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 1, item)
            else:
                if isinstance(values, list):
                    table.setRowCount(len(values))
                    for row, value in enumerate(values):
                        table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                        item = QTableWidgetItem("{:.3f}".format(value)) 
                        item.setTextAlignment(Qt.AlignCenter) 
                        table.setItem(row, 1, item)
                else:
                    table.setRowCount(1)
                    table.setItem(0, 0, QTableWidgetItem(str(title)))
                    item = QTableWidgetItem("{:.3f}".format(values)) 
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(0, 1, item)

        self.mode_label.setText(f"Мода: {results['Mode']}")
        self.median_label.setText(f"Медіана: {results['Median']}")
        self.mean_label.setText(f"Математичне сподівання: {results['Mean']}")
        self.variance_label.setText(f"Дисперсія: {results['Variance']}")
        self.std_deviation_label.setText(f"Середнє квадратичне відхилення: {results['Standard Deviation']}")

        frequency_polygon_path = calculate_frequency_polygon(numbers)
        cumulative_curve_path = calculate_cumulative_curve(numbers)
        skewness_graph_path = calculate_skewness_graph(numbers)
        kurtosis_graph_path = calculate_kurtosis_graph(numbers)

        self.label_frequency_polygon.setPixmap(QPixmap(frequency_polygon_path))
        self.label_cumulative_curve.setPixmap(QPixmap(cumulative_curve_path))
        self.label_skewness.setPixmap(QPixmap(skewness_graph_path))
        self.label_kurtosis.setPixmap(QPixmap(kurtosis_graph_path))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = MainWindow()
    window.showMaximized()
    window.show()

    sys.exit(app.exec_())
