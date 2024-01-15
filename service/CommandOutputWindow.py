# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/12/14 14:24
import sys

from PySide6.QtCore import QProcess
from PySide6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QApplication


class CommandOutputWindow(QMainWindow):
    def __init__(self):
        super(CommandOutputWindow, self).__init__()

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # self.run_command_button = QPushButton('Run Command', self)
        # self.run_command_button.clicked.connect(self.run_command)
        # self.statusBar().addWidget(self.run_command_button)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def handle_output(self, con):
        self.text_edit.append(con)


