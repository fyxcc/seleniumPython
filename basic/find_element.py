#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from util.read_ini import ReadIni
from selenium import webdriver


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key,node):
        read_ini = ReadIni(node=node)  # 实例化配置文件
        data = read_ini.get_value(key)
        by = data.split('>')[0]  # 获取配置文件中的定位方式
        value = data.split('>')[1]  # 获取定位值
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_className(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            # 截图操作
            # file_path = '../image/no_element.png'
            # self.driver.save_screenshot('../image/%s.png' % value),后期改变在teardown去执行截图操作
            return None


if __name__ == "__main__":
    register_url = 'http://localhost:9090/exam-place/login'
    driver = webdriver.Chrome()
    driver.get(register_url)
    fe = FindElement()


