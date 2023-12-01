# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'env.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, EditableComboBox, LineEdit,
                            PrimaryPushSettingCard, PushButton, StrongBodyLabel, SubtitleLabel,
                            SwitchButton, ToggleButton, PushSettingCard, FluentIcon)

from config.Config import Config


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(668, 536)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel = SubtitleLabel(Frame)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(Frame)
        self.CardWidget.setObjectName(u"CardWidget")
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.verticalLayout_2.addWidget(self.StrongBodyLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rpc_title = BodyLabel(self.CardWidget)
        self.rpc_title.setObjectName(u"rpc_title")

        self.horizontalLayout.addWidget(self.rpc_title)

        self.RpcComboBox = EditableComboBox(self.CardWidget)
        self.RpcComboBox.setObjectName(u"RpcComboBox")

        self.horizontalLayout.addWidget(self.RpcComboBox)

        self.hj_title = BodyLabel(self.CardWidget)
        self.hj_title.setObjectName(u"hj_title")

        self.horizontalLayout.addWidget(self.hj_title)

        self.HjComboBox = EditableComboBox(self.CardWidget)
        self.HjComboBox.setObjectName(u"HjComboBox")

        self.horizontalLayout.addWidget(self.HjComboBox)

        self.mk_title = BodyLabel(self.CardWidget)
        self.mk_title.setObjectName(u"mk_title")

        self.horizontalLayout.addWidget(self.mk_title)

        self.MkComboBox = EditableComboBox(self.CardWidget)
        self.MkComboBox.setObjectName(u"MkComboBox")

        self.horizontalLayout.addWidget(self.MkComboBox)

        self.shuaxinBtn = PushButton(self.CardWidget)
        self.shuaxinBtn.setObjectName(u"shuaxinBtn")

        self.horizontalLayout.addWidget(self.shuaxinBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.nginxSelect = PushSettingCard('选择',
                                           FluentIcon.DOWNLOAD,
                                           "Nginx目录",
                                           Config().fconfig.get(Config().fconfig.NginxPathFolder),
                                           self.CardWidget)
        self.nginxSelect.setObjectName(u"nginxCard")
        self.nginxSelect.setGeometry(QRect(20, 100, 621, 61))

        self.verticalLayout_2.addWidget(self.nginxSelect)


        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Frame)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.StrongBodyLabel_2 = StrongBodyLabel(self.CardWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.verticalLayout_3.addWidget(self.StrongBodyLabel_2)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hoststitle = BodyLabel(self.CardWidget_2)
        self.hoststitle.setObjectName(u"hoststitle")

        self.horizontalLayout_3.addWidget(self.hoststitle)

        self.hostjiazaiBtn = PushButton(self.CardWidget_2)
        self.hostjiazaiBtn.setObjectName(u"hostjiazaiBtn")

        self.horizontalLayout_3.addWidget(self.hostjiazaiBtn)

        self.hostswitchBtn = SwitchButton(self.CardWidget_2)
        self.hostswitchBtn.setObjectName(u"hostswitchBtn")

        self.horizontalLayout_3.addWidget(self.hostswitchBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rpctitle = BodyLabel(self.CardWidget_2)
        self.rpctitle.setObjectName(u"rpctitle")

        self.horizontalLayout_4.addWidget(self.rpctitle)

        self.rpcjiazaiBtn = PushButton(self.CardWidget_2)
        self.rpcjiazaiBtn.setObjectName(u"rpcjiazaiBtn")

        self.horizontalLayout_4.addWidget(self.rpcjiazaiBtn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.nginxtitle = BodyLabel(self.CardWidget_2)
        self.nginxtitle.setObjectName(u"nginxtitle")

        self.horizontalLayout_4.addWidget(self.nginxtitle)

        self.nginxjiazaiBtn = PushButton(self.CardWidget_2)
        self.nginxjiazaiBtn.setObjectName(u"nginxjiazaiBtn")

        self.horizontalLayout_4.addWidget(self.nginxjiazaiBtn)

        self.nginxToolBtn = ToggleButton("启动Nginx", self.CardWidget_2, FluentIcon.PLAY)
        self.nginxToolBtn.setObjectName(u"nginxToolBtn")

        self.horizontalLayout_4.addWidget(self.nginxToolBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.CardWidget_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", u"\u73af\u5883\u5207\u6362", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"\u914d\u7f6e", None))
        self.rpc_title.setText(QCoreApplication.translate("Frame", u"RPC\u914d\u7f6e", None))
        self.hj_title.setText(QCoreApplication.translate("Frame", u"HOST", None))
        self.mk_title.setText(QCoreApplication.translate("Frame", u"NginxConf", None))
        self.shuaxinBtn.setText(QCoreApplication.translate("Frame", u"\u5237\u65b0", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Frame", u"\u64cd\u4f5c", None))
        self.hoststitle.setText(QCoreApplication.translate("Frame", u"Hosts\u64cd\u4f5c\uff1a", None))
        self.hostjiazaiBtn.setText(QCoreApplication.translate("Frame", u"\u52a0\u8f7dHosts", None))
        self.hostswitchBtn.setText(QCoreApplication.translate("Frame", u"\u89e3\u5f00\u6ce8\u91ca", None))
        self.rpctitle.setText(QCoreApplication.translate("Frame", u"RPC\u914d\u7f6e", None))
        self.rpcjiazaiBtn.setText(QCoreApplication.translate("Frame", u"\u52a0\u8f7dRPC\u914d\u7f6e", None))
        self.nginxtitle.setText(QCoreApplication.translate("Frame", u"Nginx\u914d\u7f6e", None))
        self.nginxjiazaiBtn.setText(QCoreApplication.translate("Frame", u"\u52a0\u8f7dNginx\u914d\u7f6e", None))
        self.nginxToolBtn.setText(QCoreApplication.translate("Frame", u"\u542f\u52a8Nginx", None))
    # retranslateUi

