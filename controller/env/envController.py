# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/9 16:46
from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import ConfigItem, FolderValidator

import Windows
from service.core.Controller import Controller
from resource.ui.env import Ui_Frame as DEV_Frame


class Environment(Controller):
    def __init__(self, UI: Windows.Window):
        super().__init__(UI)
        self.component: DEV_Frame = self.component if self.component else None


    def bind(self):
        self.component = self.ui.dev_frame
        # 绑定选择nginx目录
        self.component.nginxSelect.clicked.connect(lambda : self.__onDownloadFolderCardClicked())


    def __onDownloadFolderCardClicked(self):
        """ download folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(
            self.component.nginxSelect, "选择文件夹", "./")
        if not folder or self.config.fconfig.get(self.config.fconfig.NginxPathFolder) == folder:
            return

        self.config.fconfig.set(self.config.fconfig.NginxPathFolder, folder)
        self.component.nginxSelect.setContent(folder)
