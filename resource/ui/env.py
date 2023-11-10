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
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, EditableComboBox, LineEdit,
                            PrimaryPushSettingCard, StrongBodyLabel, SubtitleLabel, FluentIcon, FolderValidator,
                            ConfigItem, PushSettingCard)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(668, 536)
        self.Frame = Frame
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SubtitleLabel = SubtitleLabel(Frame)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)

        self.CardWidget = CardWidget(Frame)
        self.CardWidget.setObjectName(u"CardWidget")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(20, 10, 113, 19))
        self.horizontalLayoutWidget = QWidget(self.CardWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 421, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BodyLabel = BodyLabel(self.horizontalLayoutWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.horizontalLayout.addWidget(self.BodyLabel)

        self.EditableComboBox = EditableComboBox(self.horizontalLayoutWidget)
        self.EditableComboBox.setObjectName(u"EditableComboBox")

        self.horizontalLayout.addWidget(self.EditableComboBox)

        self.BodyLabel_2 = BodyLabel(self.horizontalLayoutWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.horizontalLayout.addWidget(self.BodyLabel_2)

        self.EditableComboBox_2 = EditableComboBox(self.horizontalLayoutWidget)
        self.EditableComboBox_2.setObjectName(u"EditableComboBox_2")

        self.horizontalLayout.addWidget(self.EditableComboBox_2)

        self.widget = PushSettingCard("选择",
                                             FluentIcon.DOWNLOAD,
                                             "Nginx目录",
                                             ConfigItem(
                                                 "Folders", "Download", "app/download", FolderValidator()).value,self.CardWidget)
        self.widget.setObjectName(u"nginxCard")
        self.widget.setGeometry(QRect(20, 100, 621, 61))

        self.verticalLayout.addWidget(self.CardWidget)

        self.CardWidget_2 = CardWidget(Frame)
        self.CardWidget_2.setObjectName(u"CardWidget_2")

        self.verticalLayout.addWidget(self.CardWidget_2)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Frame", u"\u73af\u5883\u5207\u6362", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"\u914d\u7f6e", None))
        self.BodyLabel.setText(QCoreApplication.translate("Frame", u"\u73af\u5883", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Frame", u"\u6a21\u5757", None))
    # retranslateUi

