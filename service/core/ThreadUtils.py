# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/2 9:54
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


class ThreadUtils:
    _instance = None
    Threadset = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(ThreadUtils, cls).__new__(cls)
        return cls._instance

    # 创建线程池
    def __init__(self):
        # 单例似乎失效了，用这个防止init被执行
        if not hasattr(self, 'initialized'):
            self.initialized = True
            print("config initialized")
        else:
            return
        self.Threadset = ThreadPoolExecutor(max_workers=int(multiprocessing.cpu_count()/2))