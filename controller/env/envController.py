# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/9 16:46
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import ConfigItem, FolderValidator, RoundMenu, FluentIcon, ToggleButton

import Windows
from service.core.Controller import Controller
from res.ui.env import Ui_Frame as DEV_Frame

from service.envService import envService


class Environment(Controller):
    def __init__(self, UI: Windows.Window):
        super().__init__(UI)
        self.menu = None
        self.component: DEV_Frame = self.component if self.component else None
        self.service = envService(self.ui, self.config)
        self.init()
        self.otherUIInit()

    def init(self):
        # 初始化数据
        # RPC
        self.service.initComponentData()

    def bind(self):
        self.component = self.ui.dev_frame
        # 绑定选择nginx目录
        self.component.nginxSelect.clicked.connect(lambda: self.__onDownloadFolderCardClicked())
        self.component.nginxToolBtn.clicked.connect(lambda: self.service.nginxStart())
        self.component.hostjiazaiBtn.clicked.connect(
            lambda: self.service.uncomment_host(self.component.HjComboBox.text().split("-")[1],
                                                self.component.hostswitchBtn.isChecked()))
        self.component.hostswitchBtn.checkedChanged.connect(lambda: self.service.checkedChangedFunction())
        self.component.shuaxinBtn.clicked.connect(lambda: self.service.shuaxingData())
        self.component.rpcjiazaiBtn.clicked.connect(lambda: self.service.replace_file_content(
            f"C:/{self.component.RpcComboBox.text()}", "C:/setuIntegratedConfiguration.xml"))

        self.component.nginxjiazaiBtn.clicked.connect(lambda: self.service.replace_file_content(
            f"{self.config.fconfig.get(self.config.fconfig.NginxPathFolder)}/conf/{self.component.MkComboBox.text()}",
            f"{self.config.fconfig.get(self.config.fconfig.NginxPathFolder)}/conf/nginx.conf"))

    def otherUIInit(self):
        """
        其他控件内容初始化
        :return:
        """
        # Nginx按钮配置
        # self.menu = RoundMenu(self.component.nginxSelect)
        # self.menu.addAction(QAction(FluentIcon.SEND_FILL.icon(), '启动Nginx'))
        # self.menu.addAction(QAction(FluentIcon.STOP_WATCH.icon(), '停止Nginx'))
        # self.component.nginxToolBtn.setMenu(self.menu)
        # self.component.hostswitchB

    def __onDownloadFolderCardClicked(self):
        """ download folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(
            self.component.nginxSelect, "选择文件夹", "./")
        if not folder or self.config.fconfig.get(self.config.fconfig.NginxPathFolder) == folder:
            return
        # 保存内容到配置文件
        self.config.fconfig.set(self.config.fconfig.NginxPathFolder, folder)
        self.component.nginxSelect.setContent(folder)
