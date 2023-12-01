# -*- coding: utf-8 -*-            
# @Author : Lightr
# @Time : 2023/11/29 12:31
import os
import re
import subprocess

import psutil
from qfluentwidgets import FluentIcon

import Windows
from res.ui.env import Ui_Frame
from service.core.ThreadUtils import ThreadUtils
from utils.GlobalTools import GlobalTools


class envService:
    __hosts_path = r'C:\Windows\System32\drivers\etc\hosts'  # 替换为你的 hosts 文件路径
    __hostsItems = []

    def __init__(self, component: Windows.Window, config):
        self.ui = component
        self.__component: Ui_Frame = component.dev_frame
        self.fconfig = config.fconfig
        self.log = config.glog
        self.utils: GlobalTools = config.utils
        self.thread: ThreadUtils.Threadset = config.thread

    def nginxStart(self):
        self.thread.submit(self.__nginxStartAsync())

    def __nginxStartAsync(self):
        nginxPath = f"{self.fconfig.get(self.fconfig.NginxPathFolder)}"
        nginxConf = f"{self.fconfig.get(self.fconfig.NginxPathFolder)}/conf/nginx.conf"
        if self.__component.nginxToolBtn.isChecked():
            self.log.info("启动Nginx...")
            try:
                # 使用subprocess调用启动Nginx的命令，指定可执行文件路径
                self.log.info(f"Nginx路径:{nginxPath}")
                self.log.info(f"Nginx配置路径:{nginxConf}")
                self.log.info("启动")
                if self.is_nginx_running():
                    raise ValueError("Nginx已经在运行了!")
                subprocess.Popen([f"{nginxPath}/nginx.exe", "-c", f"{nginxConf}", "-p", f"{nginxPath}"])
                self.log.info("Nginx启动成功！")
                self.__component.nginxToolBtn.setText("停止Nginx")
                self.__component.nginxToolBtn.setIcon(FluentIcon.PAUSE_BOLD)
                # self.__component.nginxToolBt
                self.utils.showBarSuccessful("信息", "Nginx启动成功!")
            except Exception as e:
                self.log.error(f"Nginx启动失败: {e}")
                self.__component.nginxToolBtn.setChecked(False)
                self.utils.showBarFailure("Nginx启动失败:", f"{e}")

        else:
            try:
                self.log.info("关闭Nginx...")
                subprocess.Popen([f"{nginxPath}/nginx.exe", "-s", "stop", "-p", f"{nginxPath}"])
                self.__component.nginxToolBtn.setText("启动Nginx")
                self.__component.nginxToolBtn.setIcon(FluentIcon.PLAY)
                self.utils.showBarSuccessful("信息", "Nginx已停止")
            except Exception as e:
                self.log.error(f"Nginx停止失败: {e}")
                self.__component.nginxToolBtn.setChecked(True)
                self.utils.showBarFailure("Nginx停止失败:", f"{e}")

    def is_nginx_running(self):
        """
        判断Nginx是否在运行
        :return:
        """
        for process in psutil.process_iter(['pid', 'name']):
            if 'nginx' in process.info['name']:
                return True
        return False

    def uncomment_host(self, domain, comment: bool):
        """
        HOST添加或者解开注释
        :param comment: 是否添加或者解开注释
        :return:
        """
        try:
            self.log.info(f"修改hosts文件...: domain:{domain} comment:{comment}")
            # 读取 hosts 文件内容，并使用默认的系统编码
            with open(self.__hosts_path, 'r', encoding='mbcs') as file:
                lines = file.readlines()

            # 找到目标域名的注释行并取消注释
            with open(self.__hosts_path, 'w', encoding='mbcs') as file:
                for line in lines:
                    # 使用正则表达式匹配以 # 注释 或 未注释 的 IP 域名格式
                    match = re.match(r'^\s*#?\s*(\S+)\s+(\S+)\s*$', line)
                    if match is None:
                        continue
                    if match and match.group(2) == domain:
                        self.log.debug(f'匹配到域名:{domain}')
                        # 取消注释并去除多余的空白字符
                        if comment:
                            file.write(f"# {match.group(1)} {match.group(2)}\n")
                        else:
                            file.write(f"{match.group(1)} {match.group(2)}\n")
                    else:
                        file.write(line)
            self.utils.showBarSuccessful("Hosts文件", "Hosts文件修改成功!")
        except FileNotFoundError:
            self.utils.showBarFailure("Hosts文件不存在", f" {self.__hosts_path}")
        except Exception as e:
            self.utils.showBarFailure("Hosts文件操作失败", e)
        finally:
            # 修改完后重新获取列表
            self.log.info("重新获取HOSTS列表")
            self.setItemHost()

    def get_host(self) -> list:
        """
        获取HOSTS内容  ip domain
        :return:
        """
        self.__hostsItems = []
        try:
            # 读取 hosts 文件内容，并指定编码为 mbcs
            with open(self.__hosts_path, 'r', encoding='mbcs') as file:
                lines = file.readlines()
            for line in lines:
                zhushi = ""
                if "#" in line:
                    zhushi = "#"
                # 使用正则表达式匹配以 # 注释 或 未注释 的 IP 域名格式
                match = re.match(r'^\s*#?\s*(\S+)\s+(\S+)\s*$', line)
                if match is None:
                    continue
                self.__hostsItems.append([f"{zhushi}{match.group(1)}", match.group(2)])
        except Exception as e:
            self.utils.showBarFailure("获取HOSTS文件失败", e)
        finally:
            return self.__hostsItems

    def checkedChangedFunction(self):
        if self.__component.hostswitchBtn.isChecked():
            self.__component.hostswitchBtn.setText("添加注释")
        else:
            self.__component.hostswitchBtn.setText("解开注释")

    def setItemHost(self):
        # HOST
        hostlist = self.get_host()
        self.__component.HjComboBox.clear()
        for h in hostlist:
            self.__component.HjComboBox.addItem(f"{h[0]}-{h[1]}")

    def initComponentData(self):
        """
        初始化一些组件数据、刷新
        :return:
        """
        self.log.info("Initialized 初始化组件数据")
        self.__component.RpcComboBox.clear()
        rpcList = self.utils.read_files_in_directory("C:/", '.xml')
        for rf in rpcList:
            self.__component.RpcComboBox.addItem(rf)
        # NginxConfig
        Ngpath = f"{self.fconfig.get(self.fconfig.NginxPathFolder)}/conf"
        confList = self.utils.read_files_in_directory(Ngpath, '.conf')
        self.__component.MkComboBox.clear()
        for cf in confList:
            self.__component.MkComboBox.addItem(cf)
        # Host
        self.setItemHost()
        self.log.info("Initialized 初始化组件数据结束")

    def shuaxingData(self):
        """
        刷新按钮刷新数据
        :return:
        """
        try:
            self.initComponentData()
            self.utils.showBarSuccessful("信息", "刷新数据成功")
        except Exception as e:
            self.utils.showBarFailure("错误", e)

    def replace_file_content(self, source_file_path, target_file_path):
        try:
            # 检查源文件是否存在
            if not os.path.exists(source_file_path):
                self.log.error(f"Error: 源文件'{source_file_path}' 不存在.")
                return

            # 如果目标文件不存在，则创建目标文件
            if not os.path.exists(target_file_path):
                with open(target_file_path, 'x'):
                    pass  # 创建一个空文件
            # 读取源文件的内容
            with open(source_file_path, 'r') as source_file:
                source_content = source_file.read()

            # 将源文件的内容写入目标文件
            with open(target_file_path, 'w') as target_file:
                target_file.write(source_content)
            self.utils.showBarSuccessful("信息","替换成功!")
        except Exception as e:
            self.utils.showBarFailure("替换文件失败", e)
