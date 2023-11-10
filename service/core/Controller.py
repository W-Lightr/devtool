# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:49
# 组件都继承他
from abc import abstractmethod

import Windows
from config.Config import Config


class Controller:
    _subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._subclasses.append(cls)

    def __init__(self, UI: Windows.Window):
        # 初始化常用类
        self.ui = UI
        self.config = Config()
        self.log = self.config.glog
        self.thread = self.config.thread
        self.bind()

    @abstractmethod
    def bind(self):
        """
        用于绑定控件的
        :return:
        """
        pass
