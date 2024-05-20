import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QTabWidget
from PyQt5.QtGui import QColor, QPalette, QPixmap  
from PyQt5.QtCore import Qt 
from data_processing import process_data  
from plotting import calculate_frequency_polygon, calculate_cumulative_curve
import numpy as np
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Statistics Calculator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout() 
        self.central_widget.setLayout(self.layout)

        input_container_layout = QVBoxLayout()  
        self.input_label = QLabel("Enter numbers (separated by space):")
        self.input_field = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(lambda: self.calculate_callback())

        input_container_layout.addWidget(self.input_label)
        input_container_layout.addWidget(self.input_field)
        input_container_layout.addWidget(self.calculate_button)

        self.layout.addLayout(input_container_layout)

        # Create a tab widget
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # Create two tabs
        self.tab_frequency_polygon = QWidget()
        self.tab_cumulative_curve = QWidget()
        self.tab_widget.addTab(self.tab_frequency_polygon, "Frequency Polygon")
        self.tab_widget.addTab(self.tab_cumulative_curve, "Cumulative Curve")

        # Layouts for each tab
        self.layout_frequency_polygon = QVBoxLayout()
        self.layout_cumulative_curve = QVBoxLayout()
        self.tab_frequency_polygon.setLayout(self.layout_frequency_polygon)
        self.tab_cumulative_curve.setLayout(self.layout_cumulative_curve)

        # Tables layout
        tables_container = QWidget()  # Create a QWidget to contain the QGridLayout
        tables_layout = QGridLayout(tables_container)
        self.tables = []
        for i, title in enumerate(["Variation Series", "Statistical Distribution", "Relative Frequencies", "Cumulative Frequencies", "Relative Cumulative Frequencies"]):
            table = QTableWidget()
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(["Statistic", "Value"])
            self.tables.append(table)
            tables_layout.addWidget(QLabel(f"<b>{title}</b>"), 0, i)
            tables_layout.addWidget(table, 1, i)

        self.layout.addWidget(tables_container)

        self.mode_label = QLabel()
        self.median_label = QLabel()
        self.mean_label = QLabel()
        self.variance_label = QLabel()
        self.std_deviation_label = QLabel()

        self.layout.addWidget(self.mode_label)
        self.layout.addWidget(self.median_label)
        self.layout.addWidget(self.mean_label)
        self.layout.addWidget(self.variance_label)
        self.layout.addWidget(self.std_deviation_label)

        # Placeholder labels for frequency polygon and cumulative curve images
        self.label_frequency_polygon = QLabel("Frequency Polygon will be displayed here")
        self.label_cumulative_curve = QLabel("Cumulative Curve will be displayed here")
        self.layout_frequency_polygon.addWidget(self.label_frequency_polygon)
        self.layout_cumulative_curve.addWidget(self.label_cumulative_curve)

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

        self.mode_label.setText(f"Mode: {results['Mode']}")
        self.median_label.setText(f"Median: {results['Median']}")
        self.mean_label.setText(f"Mean: {results['Mean']}")
        self.variance_label.setText(f"Variance: {results['Variance']}")
        self.std_deviation_label.setText(f"Standard Deviation: {results['Standard Deviation']}")

        # Calculate and update frequency polygon
        frequency_polygon_path = calculate_frequency_polygon(numbers)
        frequency_pixmap = QPixmap(frequency_polygon_path)
        self.label_frequency_polygon.setPixmap(frequency_pixmap)

        # Calculate and update cumulative curve
        cumulative_curve_path = calculate_cumulative_curve(numbers)
        cumulative_pixmap = QPixmap(cumulative_curve_path)
        self.label_cumulative_curve.setPixmap(cumulative_pixmap)

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
    sys.exit(app.exec_())
