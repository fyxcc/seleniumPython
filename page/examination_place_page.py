#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import unittest
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from basic.find_element import FindElement
from selenium import webdriver

from case.login_keyword_cases import LoginKeywordCases
import HTMLTestRunner


class ExaminationPlacePage(object):
    # 初始化元素查找类，执行该类的时候就会加载
    def __init__(self, driver):
        self.driver = driver
        self.fe = FindElement(driver)

    # 考点编号
    def get_place_code(self):
        return self.fe.get_element('place_code', 'ExaminationPlacePage')

    # 考点名称
    def get_place_name(self):
        return self.fe.get_element('place_name', 'ExaminationPlacePage')

    # 行政区划
    def get_place_division_code(self):
        return self.fe.get_element('place_division_code', 'ExaminationPlacePage')

    # 行政区划市级子菜单
    def get_place_division_code_fchild(self):
        return self.fe.get_element('place_division_code_fchild', 'ExaminationPlacePage')

    # 行政区划市级子菜单
    def get_place_division_code_schild(self):
        return self.fe.get_element('place_division_code_schild', 'ExaminationPlacePage')

    # 行政区划市级子菜单
    def get_place_division_code_tchild(self):
        return self.fe.get_element('place_division_code_tchild', 'ExaminationPlacePage')

    # 考点地址
    def get_place_address(self):
        return self.fe.get_element('place_address', 'ExaminationPlacePage')

    # 考点负责人
    def get_place_person(self):
        return self.fe.get_element('place_person', 'ExaminationPlacePage')

    # 负责人联系电话
    def get_place_person_tel(self):
        return self.fe.get_element('place_person_tel', 'ExaminationPlacePage')

    # 状态
    def get_place_status(self):
        return self.fe.get_element('place_status', 'ExaminationPlacePage')

    # 状态值

    def get_place_status_value(self):
        return self.fe.get_element('place_status_value', 'ExaminationPlacePage')

    # 考点编号提示语
    def get_place_code_placeholder(self):
        print(self.fe.get_element('place_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_code', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点名称提示语
    def get_place_name_placeholder(self):
        print(self.fe.get_element('place_name', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_name', 'ExaminationPlacePage').get_attribute('placeholder')

    # 行政区划提示语
    def get_place_division_code_placeholder(self):
        print(self.fe.get_element('place_division_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_division_code', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点地址提示语
    def get_place_address_placeholder(self):
        print(self.fe.get_element('place_address', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_address', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点负责人提示语
    def get_place_person_placeholder(self):
        print(self.fe.get_element('place_person', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_person', 'ExaminationPlacePage').get_attribute('placeholder')

    # 考点负责人联系电话提示语
    def get_place_person_tel_placeholder(self):
        print(self.fe.get_element('place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder')

    # 确定添加按钮
    def get_confirm_add_btn(self):
        return self.fe.get_element('confirm_add_btn', 'ExaminationPlacePage')

    # 取消添加按钮
    def get_cancle_add_btn(self):
        return self.fe.get_element('cancle_add_btn', 'ExaminationPlacePage')

    # 添加按钮
    def get_add_btn(self):
        return self.fe.get_element('add_btn', 'ExaminationPlacePage')

    # 不合法考点编号提示语
    def get_place_code_error(self):
        return self.fe.get_element('place_code_error', 'ExaminationPlacePage')

    # 不合法考点名称示语
    def get_place_name_error(self):
        return self.fe.get_element('place_name_error', 'ExaminationPlacePage')

    # 不合法行政区划提示语
    def get_place_division_code_error(self):
        return self.fe.get_element('place_division_code_error', 'ExaminationPlacePage')

    # 不合法考点地址提示语
    def get_place_address_error(self):
        return self.fe.get_element('place_address_error', 'ExaminationPlacePage')

    # 不合法考点负责人划提示语
    def get_place_person_error(self):
        return self.fe.get_element('place_person_error', 'ExaminationPlacePage')

    # 不合法负责人联系电话提示语
    def get_place_person_tel_error(self):
        return self.fe.get_element('place_person_tel_error', 'ExaminationPlacePage')

    # 添加验证通过提示语
    def get_verify_login_error(self):
        return self.fe.get_element('verify_login_error', 'ExaminationPlacePage')

    # 添加验证不通过提示语
    def get_verify_login_error(self):
        return self.fe.get_element('verify_login_error', 'ExaminationPlacePage')

    # 获取添加考点弹框
    def get_add_frame(self):
        return self.fe.get_element('add_frame', 'ExaminationPlacePage')

    # 添加成功提示语
    def add_success(self):
        return self.fe.get_element('add_success', 'ExaminationPlacePage')

    # 删除考点按钮
    def get_delete_examination_place_btn(self):
        return self.fe.get_element('delete_examination_place_btn', 'ExaminationPlacePage')

    # 获取删除考点弹框
    def get_delete_frame(self):
        return self.fe.get_element('delete_frame', 'ExaminationPlacePage')

    # 确认删除按钮
    def get_confirm_delete_btn(self):
        sleep(1)
        return self.fe.get_element('confirm_delete', 'ExaminationPlacePage')

    # 取消删除按钮
    def get_cancle_delete_btn(self):
        return self.fe.get_element('cancle_delete', 'ExaminationPlacePage')

    # 定位删除考点失败提示信息
    def get_delete_examination_place_result(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath('/html/body/div[17]/div/div'))
        return self.driver.find_element_by_xpath('/html/body/div[17]/div/div').text

    # 编辑考点编号
    def get_edit_place_code(self):
        return self.fe.get_element('edit_place_code', 'ExaminationPlacePage')

    # 编辑考点名称
    def get_edit_place_name(self):
        return self.fe.get_element('edit_place_name', 'ExaminationPlacePage')

    # 编辑行政区划
    def get_edit_place_division_code(self):
        return self.fe.get_element('edit_place_division_code', 'ExaminationPlacePage')

    # 清除行政区划
    def clear_place_division_code(self):
        return self.fe.get_element('edit_place_division_code', 'ExaminationPlacePage')

    # 编辑行政区划市级子菜单
    def get_edit_place_division_code_fchild(self):
        return self.fe.get_element('edit_place_division_code_fchild', 'ExaminationPlacePage')

    # 编辑行政区划市级子菜单
    def get_edit_place_division_code_schild(self):
        return self.fe.get_element('edit_place_division_code_schild', 'ExaminationPlacePage')

    # 编辑行政区划市级子菜单
    def get_edit_place_division_code_tchild(self):
        return self.fe.get_element('edit_place_division_code_tchild', 'ExaminationPlacePage')

    # 编辑考点地址
    def get_edit_place_address(self):
        return self.fe.get_element('edit_place_address', 'ExaminationPlacePage')

    # 编辑考点负责人
    def get_edit_place_person(self):
        return self.fe.get_element('edit_place_person', 'ExaminationPlacePage')

    # 编辑负责人联系电话
    def get_edit_place_person_tel(self):
        return self.fe.get_element('edit_place_person_tel', 'ExaminationPlacePage')

    # 编辑状态
    def get_edit_place_status(self):
        return self.fe.get_element('edit_place_status', 'ExaminationPlacePage')

    #  编辑状态值

    def get_edit_place_status_value(self):
        return self.fe.get_element('edit_place_status_value', 'ExaminationPlacePage')

    #  编辑考点编号提示语
    def get_edit_place_code_placeholder(self):
        print(self.fe.get_element('edit_place_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_code', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑考点名称提示语
    def get_edit_place_name_placeholder(self):
        print(self.fe.get_element('edit_place_name', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_name', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑行政区划提示语
    def get_edit_place_division_code_placeholder(self):
        print(self.fe.get_element('edit_place_division_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_division_code', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑考点地址提示语
    def get_edit_place_address_placeholder(self):
        print(self.fe.get_element('edit_place_address', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_address', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑考点负责人提示语
    def get_edit_place_person_placeholder(self):
        print(self.fe.get_element('edit_place_person', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_person', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑考点负责人联系电话提示语
    def get_edit_place_person_tel_placeholder(self):
        print(self.fe.get_element('edit_place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('edit_place_person_tel', 'ExaminationPlacePage').get_attribute('placeholder')

    #  编辑确定添加按钮
    def get_edit_confirm_btn(self):
        return self.fe.get_element('edit_confirm_btn', 'ExaminationPlacePage')

    #  编辑取消添加按钮
    def get_edit_cancle_btn(self):
        return self.fe.get_element('edit_cancle_btn', 'ExaminationPlacePage')

    #  编辑添加按钮
    def get_edit_btn(self):
        return self.fe.get_element('edit_btn', 'ExaminationPlacePage')

    #  编辑不合法考点编号提示语
    def get_edit_place_code_error(self):
        return self.fe.get_element('edit_place_code_error', 'ExaminationPlacePage')

    #  编辑不合法考点名称示语
    def get_edit_place_name_error(self):
        return self.fe.get_element('edit_place_name_error', 'ExaminationPlacePage')

    #  编辑不合法行政区划提示语
    def get_edit_place_division_code_error(self):
        return self.fe.get_element('edit_place_division_code_error', 'ExaminationPlacePage')

    #  编辑不合法考点地址提示语
    def get_edit_place_address_error(self):
        return self.fe.get_element('edit_place_address_error', 'ExaminationPlacePage')

    #  编辑不合法考点负责人划提示语
    def get_edit_place_person_error(self):
        return self.fe.get_element('edit_place_person_error', 'ExaminationPlacePage')

    #  编辑不合法负责人联系电话提示语
    def get_edit_place_person_tel_error(self):
        return self.fe.get_element('edit_place_person_tel_error', 'ExaminationPlacePage')

    #  编辑添加验证通过提示语
    def get_edit_success(self):
        return self.fe.get_element('edit_success', 'ExaminationPlacePage')

    #  编辑添加验证不通过提示语
    def get_edit_repeat_code_error(self):
        return self.fe.get_element('edit_repeat_code_error', 'ExaminationPlacePage')

    #  编辑获取添加考点弹框
    def get_edit_frame(self):
        return self.fe.get_element('edit_frame', 'ExaminationPlacePage')

    # 查询考点编号
    def get_query_place_code(self):
        return self.fe.get_element('query_place_code', 'ExaminationPlacePage')

    # 查询考点名称
    def get_query_place_name(self):
        return self.fe.get_element('query_place_name', 'ExaminationPlacePage')

    # 查询行政区划
    def get_query_place_division_code(self):
        return self.fe.get_element('query_place_division_code', 'ExaminationPlacePage')

    # 查询行政区划市级一级子菜单

    def get_query_place_division_code_fchild(self):
        return self.fe.get_element('query_place_division_code_fchild', 'ExaminationPlacePage')

    # 查询行政区划市级二级子菜单
    def get_query_place_division_code_schild(self):
        return self.fe.get_element('query_place_division_code_schild', 'ExaminationPlacePage')

    # 查询行政区划市级三级子菜单

    def get_query_place_division_code_tchild(self):
        return self.fe.get_element('query_place_division_code_tchild', 'ExaminationPlacePage')

    #  查询考点编号提示语

    def get_query_place_code_placeholder(self):
        print(self.fe.get_element('query_place_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('query_place_code', 'ExaminationPlacePage').get_attribute('placeholder')

    #  查询考点名称提示语

    def get_query_place_name_placeholder(self):
        print(self.fe.get_element('query_place_name', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('query_place_name', 'ExaminationPlacePage').get_attribute('placeholder')

    #  查询行政区划提示语

    def get_query_place_division_code_placeholder(self):
        print(self.fe.get_element('query_place_division_code', 'ExaminationPlacePage').get_attribute('placeholder'))
        return self.fe.get_element('query_place_division_code', 'ExaminationPlacePage').get_attribute('placeholder')

    # 查询按钮
    def get_query_btn(self):
        return self.fe.get_element('query_btn', 'ExaminationPlacePage')

    # 总计数目项
    def get_query_total_count(self):
        return self.fe.get_element('total_count', 'ExaminationPlacePage')

    # 查询结果数目

    def get_query_result_count(self):
        return self.fe.get_element('query_result_count', 'ExaminationPlacePage')

    # 查询已选择数目

    def get_choiced_count(self):
        return self.fe.get_element('choiced_count', 'ExaminationPlacePage')

    # 清空按钮
    def get_clear_btn(self):
        return self.fe.get_element('clear_btn', 'ExaminationPlacePage')

    # 列表考点编号
    def get_table_place_code(self):
        return self.fe.get_element('table_place_code', 'ExaminationPlacePage')

    # 列表考点名称
    def get_table_place_name(self):
        return self.fe.get_element('table_place_name', 'ExaminationPlacePage')

    # 列表行政区划
    def get_table_place_division_code(self):
        return self.fe.get_element('table_place_division_code', 'ExaminationPlacePage')

    # 列表考点地址
    def get_table_place_address(self):
        return self.fe.get_element('table_place_address', 'ExaminationPlacePage')

    # 列表考点负责人
    def get_table_place_person(self):
        return self.fe.get_element('table_place_person', 'ExaminationPlacePage')

    # 列表负责人联系电话
    def get_table_place_person_tel(self):
        return self.fe.get_element('table_place_person_tel', 'ExaminationPlacePage')

    # 列表考场数

    def get_table_exam_place_num(self):
        return self.fe.get_element('table_exam_place_num', 'ExaminationPlacePage')

    # 列表可编排机位数
    def get_table_use_computer_num(self):
        return self.fe.get_element('table_use_computer_num', 'ExaminationPlacePage')

    # 列表总机位数

    def get_table_total_computer_num(self):
        return self.fe.get_element('table_total_computer_num', 'ExaminationPlacePage')

    # 列表更新时间

    def get_table_update_time(self):
        return self.fe.get_element('table_update_time', 'ExaminationPlacePage')

    # 列表状态
    def get_table_status(self):
        return self.fe.get_element('table_status', 'ExaminationPlacePage')

    # 导出按钮
    def get_export_btn(self):
        return self.fe.get_element('export_btn', 'ExaminationPlacePage')

    # 行政区划选择取消按钮
    def get_clear_query_place_division_code(self):
        return self.fe.get_element('clear_query_place_division_code', 'ExaminationPlacePage')

    # 未查询到结果弹框
    def get_empty_result(self):
        return self.fe.get_element('empty_query_result', 'ExaminationPlacePage')

    # 确定未查询到结果弹框按钮
    def get_empty_result_btn(self):
        return self.fe.get_element('confirm_empty_query_result', 'ExaminationPlacePage')

    # 考点编号正序按钮
    def get_table_code_positive_seq(self):
        return self.fe.get_element('table_code_positive_seq', 'ExaminationPlacePage')

    # 考点编号倒序按钮

    def get_table_code_inverted_seq(self):
        return self.fe.get_element('table_code_inverted_seq', 'ExaminationPlacePage')

    # 考场数正序按钮
    def get_exam_place_num_positive_seq(self):
        return self.fe.get_element('exam_place_num_positive_seq', 'ExaminationPlacePage')

    # 考场数倒序按钮
    def get_exam_place_num_inverted_seq(self):
        return self.fe.get_element('exam_place_num_inverted_seq', 'ExaminationPlacePage')

    # 可编排机位数正序按钮
    def get_use_computer_num_positive_seq(self):
        return self.fe.get_element('use_computer_num_positive_seq', 'ExaminationPlacePage')

    # 可编排机位数倒序按钮
    def get_use_computer_num_inverted_seq(self):
        return self.fe.get_element('use_computer_num_inverted_seq', 'ExaminationPlacePage')

    # 总机位数正序按钮
    def get_table_total_computer_num_positive_seq(self):
        return self.fe.get_element('table_total_computer_num_positive_seq', 'ExaminationPlacePage')

    # 总机位数倒序按钮
    def get_table_total_computer_num_inverted_seq(self):
        return self.fe.get_element('table_total_computer_num_inverted_seq', 'ExaminationPlacePage')


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    Ep = ExaminationPlacePage(driver)
    driver.maximize_window()
