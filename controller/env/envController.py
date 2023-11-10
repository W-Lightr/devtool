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
        self.component: DEV_Frame = None

    def bind(self):
        self.component = self.ui.dev_frame
        # 绑定选择nginx目录
        self.component.widget.clicked.connect(self.onDownloadFolderCardClicked)

    def onDownloadFolderCardClicked(self):
        """ download folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(
            self.component.widget, "选择文件夹", "./")
        if not folder or ConfigItem(
                "Folders", "Download", "app/download", FolderValidator()).value == folder:
            return
        self.component.widget.setContent(folder)
