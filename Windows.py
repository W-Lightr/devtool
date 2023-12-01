# coding:utf-8
import os
import sys
from PySide6.QtCore import Qt, QRect, QUrl
from PySide6.QtGui import QIcon, QPainter, QImage, QBrush, QColor, QFont, QDesktopServices
from PySide6.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, NavigationWidget, MessageBox,
                            isDarkTheme, setTheme, Theme, setThemeColor, qrouter, NavigationAvatarWidget)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar

from res.ui.log import Ui_Frame as RZ_Frame
from res.ui.test import Ui_Frame as TEST_Frame
from res.ui.env import Ui_Frame as DEV_Frame


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        root_path = sys.path[0]
        self.project_path = os.path.abspath(os.path.join(root_path, "config"))
        # use dark theme mode
        # setTheme(Theme.DARK)
        # change the theme color
        # setThemeColor('#0078d4')
        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)
        # ================================================================
        # create sub interface 创建侧边栏功能组件
        # 日志
        self.logInterface = QFrame(self)
        self.logInterface.setObjectName("logInterface")
        # 日志页面所有组件
        self.rz_frame = RZ_Frame()
        self.rz_frame.setupUi(self.logInterface)
        # 开发环境工具
        self.devtoolInterface = QFrame(self)
        self.devtoolInterface.setObjectName("devtoolInterface")
        self.dev_frame = DEV_Frame()
        self.dev_frame.setupUi(self.devtoolInterface)
        # test组件
        # self.testInterface = QFrame(self)
        # self.testInterface.setObjectName("testInterface")
        # self.test_frame = TEST_Frame()
        # self.test_frame.setupUi(self.testInterface)

        # self.searchInterface = Widget('Search Interface', self)
        # self.musicInterface = Widget('Music Interface', self)
        # self.videoInterface = Widget('Video Interface', self)
        # self.folderInterface = Widget('Folder Interface', self)
        # self.settingInterface = Widget('Setting Interface', self)
        # self.albumInterface = Widget('Album Interface', self)
        # self.albumInterface1 = Widget('Album Interface 1', self)
        # self.albumInterface2 = Widget('Album Interface 2', self)
        # self.albumInterface1_1 = Widget('Album Interface 1-1', self)
        self.settingInterface = Widget('Setting Interface', self)
        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        # enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)
        # 添加侧边栏
        self.addSubInterface(self.logInterface, FIF.DOCUMENT, '日志', NavigationItemPosition.BOTTOM)
        # self.addSubInterface(self.testInterface, FIF.HOME, '测试')
        self.addSubInterface(self.devtoolInterface, FIF.DEVELOPER_TOOLS, '开发')
        # self.addSubInterface(self.musicInterface, FIF.MUSIC, 'Music library')
        # self.navigationInterface.addSeparator()
        # self.addSubInterface(self.testInterface, FIF.HOME, '测试')
        # self.addSubInterface(self.albumInterface1, FIF.ALBUM, 'Album 1', parent=self.albumInterface)
        # self.addSubInterface(self.albumInterface1_1, FIF.ALBUM, 'Album 1.1', parent=self.albumInterface1)
        # self.addSubInterface(self.albumInterface2, FIF.ALBUM, 'Album 2', parent=self.albumInterface)
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.settingInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

        # !IMPORTANT: don't forget to set the default route key if you enable the return button
        # qrouter.setDefaultRouteKey(self.stackWidget, self.musicInterface.objectName())

        # set the maximum width
        # self.navigationInterface.setExpandWidth(300)

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(1)

        # always expand
        # self.navigationInterface.setCollapsible(False)

    def initWindow(self):
        self.resize(900, 700)
        # self.setWindowIcon(QIcon('res/logo.png'))
        self.setWindowTitle('Lightr的小工具')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.screens()[0].availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)

        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

    def setQss(self):
        # color = 'dark' if isDarkTheme() else 'light'
        # with open(f'res/{color}/demo.qss', encoding='utf-8') as f:
        #     self.setStyleSheet(f.read())
        pass

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

        # !IMPORTANT: This line of code needs to be uncommented if the return button is enabled
        # qrouter.push(self.stackWidget, widget.objectName())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec()
