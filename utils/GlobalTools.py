# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 15:35
import glob
import os

from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarPosition


class GlobalTools:
    _instance = None

    def __new__(cls, ui, config):
        if cls._instance is None:
            cls._instance = super(GlobalTools, cls).__new__(cls)
        return cls._instance

    def __init__(self, ui, config):
        if not hasattr(self, 'initialized'):
            self.initialized = True
        else:
            return

        self.ui = ui
        self.config = config
        self.log = config.glog
    def read_files_in_directory(self, directory_path, file_extension=".json"):
        """
        读取指定目录中的文件并返回文件名列表

        参数：
        directory_path (str)：指定的目录路径
        file_extension (str, 可选)：文件扩展名，默认为".json"

        返回：
        list：文件名列表
        """

        # 使用 glob 模块获取指定格式的文件列表
        file_pattern = os.path.join(directory_path, f"*{file_extension}")
        file_list = glob.glob(file_pattern)
        file_names = []
        # 逐个获取文件名
        for file_path in file_list:
            file_name = os.path.basename(file_path)
            file_names.append(file_name)
        return file_names

    def showBarSuccessful(self, title, message):
        self.log.info(f"{title}:{message}")
        InfoBar.success(
            title=f'{title}',
            content=f"{message}",
            orient=Qt.Vertical,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=3000,
            parent=self.ui
        )

    def showBarFailure(self, title, message):
        self.log.error(f"{title}: {message}")
        InfoBar.error(
            title=f'{title}',
            content=f"{message}",
            orient=Qt.Vertical,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=3000,
            parent=self.ui
        )

    def read_hosts_file(self,file_path):
        """
        读取文件
        :param file_path:
        :return:
        """
        try:
            with open(file_path, 'r') as file:
                # 读取文件内容并使用换行符分割成行
                lines = file.read().splitlines()
                return lines
        except FileNotFoundError:
            self.log.info(f"File not found: {file_path}")
        except Exception as e:
            self.log.info(f"Error reading hosts file: {e}")