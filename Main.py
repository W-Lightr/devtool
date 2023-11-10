# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/1 14:59
import io
import os
import sys
import importlib
import Windows
from config.Config import Config
from config.Log.GlobalLog import GlobalLog
from service.core.Controller import Controller
from service.core.ThreadUtils import ThreadUtils


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
        config.Thread = ThreadUtils()

        # 其他模块初始化
        package_name = "controller"
        # 导入所有*Controller模块 且继承Controller
        self.import_modules(package_name)

        # 初始化继承controller的模块
        all_subclasses = Controller.__subclasses__()
        for subclass in all_subclasses:
            instance = subclass(self.navigation)

        # 防止print
        buffer = io.StringIO()
        sys.stdout = buffer
        sys.stderr = buffer

    # 导入模块
    def import_modules(self, package_name):
        for root, dirs, files in os.walk(package_name):
            for file in files:
                if file.endswith(".py"):
                    module_path = os.path.join(root, file)
                    module_name = module_path.replace("\\", ".").replace(".py", "")
                    if "Controller" in module_name:
                        module = importlib.import_module(module_name)
                        # 在这里你可以对每个模块执行操作，如调用模块中的函数或类
                        print(f"Imported module: {module_name}")
