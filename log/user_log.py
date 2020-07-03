# coding=utf-8


import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        # 定义日志器，提供应用程序可一直使用的接口
        self.logger = logging.getLogger()
        # 设置日志级别，设置日志器将会处理的日志消息的级别
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        self.logger.addHandler(console)
        # 输出控制台

        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        self.log_name = log_dir + "/" + log_file

        # 文件输出日志
        self.file_handle = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        # 格式化日志文件，决定日志记录的最终输出格式
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s----> %(message)s ')
        # 将文件流格式化
        self.file_handle.setFormatter(formatter)
        # 为该logger对象添加一个handler对象
        self.logger.addHandler(self.file_handle)
        # 创建一个与它们的方法名对应等级的日志记录
        self.logger.debug('test1212')

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)
    def clear_log(self):
        file=open(self.log_name,'w')
        file.close()



if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('11111')
    user.close_handle()
