# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 13:37
from service.core.Controller import Controller


class Test(Controller):
    def __init__(self, UI):
        super().__init__(UI)
        # Test的组件
        self.component = None

    def bind(self):
        pass
        # self.component = self.ui.test_frame
        # self.log.info("Binding Controller")
        # self.component.PrimaryPushButton.clicked.connect(lambda: self.log.info("Hello World"))
