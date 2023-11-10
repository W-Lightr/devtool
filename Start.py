# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:30

import sys

from PySide6.QtWidgets import QApplication
from Main import Main
from Windows import Window


# 启动类软件的类
class start:
    def __init__(self, F):
        self.Main = Main()
        self.Main.init(F)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        w = Window()
        w.move(550, 100)
        main = start(w)
        w.show()
        app.exec()
    except BaseException as f:
        print(f"程序运行出错：{f}")