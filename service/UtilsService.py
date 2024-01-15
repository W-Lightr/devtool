# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2024/1/8 18:27
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QDialog, QPushButton, QTextEdit, QVBoxLayout


# 弹出新窗口输出内容
# class LogViewer(QDialog):
#     update_signal = Signal(str)
#
#     def __init__(self, parent=None, title="提示", ):
#         super().__init__(parent)
#
#         self.setWindowTitle(title)
#         self.setFixedSize(600, 400)
#         # 创建 QTextEdit 控件用于显示日志
#         self.log_textedit = QTextEdit(self)
#         self.log_textedit.setReadOnly(True)
#         # 创建按钮用于清空日志
#         clear_button = QPushButton("清除日志", self)
#         clear_button.clicked.connect(lambda : self.update_ui("ceshi"))
#
#         # 设置布局
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.log_textedit)
#         layout.addWidget(clear_button)
#         self.update_signal.connect(lambda x: self.update_ui(x))
#
#     @Slot(str)
#     def update_ui(self, log_message):
#         self.log_textedit.append(log_message)
#
#     def clear_log(self):
#         self.log_textedit.clear()
