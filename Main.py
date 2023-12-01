# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/1 14:59
import io
import sys
import Windows
from config.Config import Config
from config.Log.GlobalLog import GlobalLog
from controller.env.envController import Environment
from service.core.ThreadUtils import ThreadUtils
from utils.GlobalTools import GlobalTools


class Main:
    def __init__(self):
        self.navigation = None

    def init(self, F: Windows.Window):
        # 初始化配置
        self.navigation = F
        config = Config()
        # 初始化日志
        # 可以在日志类中指定输出日志的控件
        self.log = GlobalLog()
        self.log.uiControl = self.navigation.rz_frame.logPlainTextEdit
        self.navigation.rz_frame.logPrimaryPushButton.clicked.connect(self.log.clearLog)
        # 定义UI 用于输出日志
        config.glog = self.log.glog
        # 初始化线程
        config.thread = ThreadUtils().Threadset
        config.utils = GlobalTools(self.navigation, config)
        # 其他模块初始化
        # 初始化env
        self.envController = Environment(self.navigation)
        # 防止print
        buffer = io.StringIO()
        sys.stdout = buffer
        sys.stderr = buffer


