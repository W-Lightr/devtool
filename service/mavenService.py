# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/12/11 16:37
import fnmatch
import os
import requests
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QPushButton, QMainWindow, QWidget

import Windows
from res.ui.env import Ui_Frame
from service.core.ThreadUtils import ThreadUtils
from utils.GlobalTools import GlobalTools


class mavenService:

    def __init__(self, component: Windows.Window, config):
        self.ui = component
        self.__component: Ui_Frame = component.dev_frame
        self.fconfig = config.fconfig
        self.log = config.glog
        self.utils: GlobalTools = config.utils
        self.thread: ThreadUtils.Threadset = config.thread
        # 保证窗口不被销毁
        self.outWindow = None

    def initComponentData(self):
        self.__component.mavenzhedit.setText(self.fconfig.get(self.fconfig.MavenUser))
        self.__component.mavenmmedit.setText(self.fconfig.get(self.fconfig.MavenPassword))
        self.__component.mavenycurledit.setText(self.fconfig.get(self.fconfig.MavenRemoteUrl))

    def upload_files_to_repo(self, repo_url, username, password):
        self.log.info("上传maven依赖......")
        self.log_viewer = LogViewer(repo_url, username, password, self.fconfig.get(self.fconfig.MavenPathFolder),
                                    title='上传日志')
        # self.log_viewer.start_upload()
        self.log_viewer.show()

    def clearZX(self):
        path = self.fconfig.get(self.fconfig.MavenPathFolder)
        self.log.info(f"清除路径:{path}")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith("_remote.repositories") or file.endswith(".lastUpdated"):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        self.log.debug(f"删除文件成功: {file_path}")
                    except Exception as e:
                        self.utils.showBarFailure("删除文件失败", e),
                        self.log.error(f"Error deleting {file_path}: {e}")
        self.utils.showBarSuccessful("提示","清除成功")
    def writeUserToFile(self, newContent):
        self.fconfig.set(self.fconfig.MavenUser, newContent)

    def writePasswordToFile(self, newContent):
        self.fconfig.set(self.fconfig.MavenPassword, newContent)

    def writeRemoterUrlToFile(self, newContent):
        self.fconfig.set(self.fconfig.MavenRemoteUrl, newContent)


class LogViewer(QMainWindow):
    def __init__(self, repo_url, username, password, scanPath, title='Log Viewer'):
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(600, 400)
        self.central_widget = QTextEdit(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QVBoxLayout(self.central_widget)
        self.worker_thread = None
        self.start_upload(repo_url, username, password, scanPath)

    def start_upload(self, repo_url, username, password, scanPath):
        self.worker_thread = UploadThread(repo_url, username, password, scanPath)
        self.worker_thread.update_signal.connect(self.update_log)
        self.worker_thread.start()

    def update_log(self, message):
        self.central_widget.append(message)

    def closeEvent(self, event):
        # 重写 closeEvent 方法，窗口关闭时发送停止线程的信号
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.finished_signal.disconnect()
            self.worker_thread.quit()
            self.worker_thread.wait()

        event.accept()
class UploadThread(QThread):
    update_signal = Signal(str)

    def __init__(self, repo_url, username, password, scanPath):
        super().__init__()
        self.repo_url = repo_url
        self.username = username
        self.password = password
        self.scanPath = scanPath

    def run(self):
        self.update_signal.emit("Uploading files")
        exclude_patterns = [
            './mavenimport.sh*',
            '*/.*',
            '*/^archetype-catalog.xml*',
            '*/^maven-metadata-local*.xml',
            '*/^maven-metadata-deployment*.xml',
            '*_remote.repositories',
            '*.lastUpdated'
        ]
        scanPath = self.scanPath  # Set your scan path
        for root, dirs, files in os.walk(scanPath):
            for filename in files:
                file_path = os.path.join(root, filename)
                if not any(fnmatch.fnmatch(file_path, pattern) for pattern in exclude_patterns):
                    fileConPath = file_path.replace("\\", "/")
                    relative_path = file_path.replace(scanPath, "")[1:]
                    full_url = f"{self.repo_url}{relative_path}".replace("\\", "/")
                    self.update_signal.emit(f"上传 {file_path} - {full_url}")
                    with open(fileConPath, 'rb') as file:
                        response = requests.put(
                            full_url,
                            auth=(self.username, self.password),
                            data=file,
                            headers={'Content-Type': 'application/octet-stream'}
                        )
                        self.update_signal.emit(f"上传 {file_path} - Status Code: {response.status_code}")
