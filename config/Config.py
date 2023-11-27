# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:40

from config.Log.MyLogger import MyLogger
from service.core.ThreadUtils import ThreadUtils
from qfluentwidgets import qconfig, QConfig, ConfigItem, FolderListValidator, Theme, FolderValidator


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # 单例似乎失效了，用这个防止init被执行
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("config initialized")
        else:
            return
        # UI控件
        # self.ui: ui.Ui_MainWindow = None
        # 日志
        self.glog: MyLogger = None
        # 线程对象
        self.thread: ThreadUtils = None
        # musicFolders = ConfigItem(
        #     "Folders", "LocalMusic", [], FolderListValidator())
        self.fconfig = FConfig()
        qconfig.load('app/config/config.json', self.fconfig)


class FConfig(QConfig):
    # dev工具的配置
    musicFolders = ConfigItem(
        "devSwitch", "LocalMusic", [], FolderListValidator())

    NginxPathFolder = ConfigItem(
        "devSwitch", "NginxPath", "app/download", FolderValidator())

    RpcConfig = ConfigItem(
        "devSwitch", "RpcConfig", "px.xml;ceshi.xml")
