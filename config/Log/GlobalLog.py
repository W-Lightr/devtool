# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:42
import logging

from config.Log.MyLogger import MyLogger, LogSignal


class GlobalLog:
    def __init__(self):
        print("初始化GlobalLog")
        # UI控件中的输入框
        self.uiControl = None
        # 控制台输出
        console_handler = logging.StreamHandler()
        # console_handler.setLevel(logging.DEBUG)
        self.glog = MyLogger("GLOG", [self._getHandler(), console_handler])
        # self.bind()

    def _getHandler(self):
        self.log_signal = LogSignal()
        self.log_signal.log_updated.connect(self.update_log_text)
        return GlobalLog.GHandler(self.log_signal)

    def update_log_text(self, msg):
        if self.uiControl is not None:
            self.uiControl.appendHtml(msg)

    def clearLog(self):
        if self.uiControl is not None:
            self.uiControl.clear()

    class GHandler(logging.Handler):
        def __init__(self, log_signal):
            logging.Handler.__init__(self)
            self.log_signal = log_signal
            self.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.setLevel(logging.DEBUG)

        def emit(self, record):
            msg = self.format(record)
            self.log_signal.log_updated.emit(msg)
