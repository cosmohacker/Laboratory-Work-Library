import os

import psutil
import matplotlib.pyplot as plt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window().setWindowIcon(QIcon('assets/icon.jpg'))
        self.setWindowTitle('Performence')
        self.setGeometry(100, 100, 800, 600)

        # Create the figure and axes for the plot
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        # Create a timer to update the plot every second
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1000 milliseconds = 1 second
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        # Initialize the data arrays
        self.cpu_data = []
        self.mem_data = []
        self.disk_data = []

        self.show()

    def update_plot(self):
        # Get the system usage data
        cpu_percent = psutil.cpu_percent()
        mem_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent

        # Add the new data to the plot
        self.cpu_data.append(cpu_percent)
        self.mem_data.append(mem_percent)
        self.disk_data.append(disk_percent)

        # Clear the plot and plot all data
        self.axes.clear()
        self.axes.plot(self.cpu_data, 'g', label='CPU')
        self.axes.plot(self.mem_data, 'b', label='Memory')
        self.axes.plot(self.disk_data, 'r', label='Disk')

        # Add a threshold line at 80% usage for each metric
        self.axes.axhline(y=80, color='k', linestyle='--')

        # Add text labels for the current value of each metric
        self.axes.text(0, cpu_percent+2, f'CPU: {cpu_percent:.2f}%')
        self.axes.text(0, mem_percent+2, f'Memory: {mem_percent:.2f}%')
        self.axes.text(0, disk_percent+2, f'Disk: {disk_percent:.2f}%')

        # Set the y limits of the plot
        self.axes.set_ylim([0, 100])

        # Add a legend to the plot
        self.axes.legend(loc='upper right')

        # Set the title of the plot with the current values
        self.figure.suptitle(f'CPU: {cpu_percent:.2f}% | Memory: {mem_percent:.2f}% | Disk: {disk_percent:.2f}%')

        # Draw the plot
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
