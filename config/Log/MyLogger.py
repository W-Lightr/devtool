# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:44
import logging
import sys

from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal


class MyLogger(QtCore.QObject):
    """
    handler:输出handler
    name:日志类名称
    """
    logUpdated = QtCore.Signal(str)

    def __init__(self, name, handlers: list):
        super().__init__()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        # self.logger.root.setLevel(logging.INFO)
        for h in handlers:
            self.logger.addHandler(h)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


class LogSignal(QObject):
    log_updated = Signal(str)
