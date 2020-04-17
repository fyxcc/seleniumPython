#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from util.table_util import TableUtil
from time import sleep


class ExaminationPlaceBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.Eh = ExaminationPlaceHandle(self.driver)
        self.Tu = TableUtil(self.driver)

    # 成功添加
    def success_add(self, place_code, place_name, place_address, place_person, place_person_tel, assertCode):
        self.Eh.send_place_code(place_code)
        self.Eh.send_place_name(place_name)
        if len(assertCode) == 0:
            self.Eh.send_place_division_code()
        self.Eh.send_place_address(place_address)
        self.Eh.send_place_person(place_person)
        self.Eh.send_place_person_tel(place_person_tel)
        # self.Eh.select_place_status()
        self.Eh.click_confirm_add_btn()
        sleep(3)

    # 数据驱动整合代码
    def add_function(self, place_code, place_name, place_address, place_person, place_person_tel, assertCode,
                     assertText):
        self.success_add(place_code, place_name, place_address, place_person, place_person_tel, assertCode)
        if len(assertCode) != 0:
            if self.Eh.get_user_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True
        else:
            if assertText == '添加成功':
                if self.Eh.get_add_success_text() == assertText:
                    print('添加成功，用例通过')
                    return True

    # 判断编辑框内容是否完整
    def edit_complete(self):
        if self.Eh.get_backfill_data() == '回填信息数据完整':
            return True
        elif self.Eh.get_backfill_data() == '回填信息数据不完整':
            return False

    # 成功编辑
    def success_edit(self, place_code, place_name, place_address, place_person, place_person_tel, assertCode):
        self.Eh.send_edit_place_code(place_code)
        self.Eh.send_edit_place_name(place_name)
        # if len(assertCode) == 0:
        # self.Eh.send_edit_place_division_code()
        self.Eh.send_edit_place_address(place_address)
        self.Eh.send_edit_place_person(place_person)
        self.Eh.send_edit_place_person_tel(place_person_tel)
        # self.Eh.select_edit_place_status()
        self.Eh.click_edit_confirm_btn()

    # 数据驱动整合代码
    def edit_function(self, place_code, place_name, place_address, place_person, place_person_tel, assertCode,
                      assertText):
        self.success_edit(place_code, place_name, place_address, place_person, place_person_tel, assertCode)
        if len(assertCode) != 0:
            if self.Eh.get_edit_user_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True
        else:
            if assertText == '编辑成功':
                sleep(2)
                if self.Eh.get_edit_success_text() == assertText:
                    print('添加成功，用例通过')
                    return True
                else:
                    print('添加失败，用例未通过')
                    return False

    # 删除考点
    def delete_examination_place(self):
        self.Eh.click_delete_examination_place_btn()
        self.Eh.click_confirm_delete_btn()
        return self.Eh.get_delete_result()

    # 判断查询页面元素是否完整
    def judge_page_complete(self):
        if self.Eh.judge_query_condition_complete() and self.Eh.judge_count_result_complete() and self.Eh.table_info_complete() and self.Eh.btn_complete():
            return True
        else:
            return False

    # 判断行政区划省市区联动查询
    def judge_query_place_division_code(self, way):
        if way == 'fchild':
            self.Eh.send_query_place_division_code_fchild()
        elif way == 'schild':
            self.Eh.send_query_place_division_code_schild()
        else:
            self.Eh.send_query_place_division_code_tchild()

    # 验证行政区划查询结果是否正确
    def judge_query_result(self):
        # 获取输入查询条件
        query_division_code_condition = self.Eh.get_place_division_code_condition()
        # 点击查询按钮
        self.Eh.click_query_btn()
        # 获取table查询总数
        total_query_nums = self.Tu.get_lines()
        # 判断查询结果和table查询结果数目是否相等
        if self.Tu.get_lines() == self.Eh.get_query_result_count_text():
            # 当查询数据存储在一页的时候
            if self.Tu.judge_click_next_page() == 0:
                for rows in range(1, total_query_nums + 1):
                    # 判断行政区划字段是否都是包含查询条件内容
                    if query_division_code_condition not in self.Tu.get_data(rows, 4):
                        return False
                return True
            # 当查询结果分页保存的时候
            else:
                # 获取点击下一页次数
                click_next_page = self.Tu.judge_click_next_page()
                # 获取table每页行数
                page_size = self.Tu.get_page_size()
                for click_nums in range(1, click_next_page + 1):
                    for rows in range(1, page_size + 1):
                        if query_division_code_condition not in self.Tu.get_data(rows, 4):
                            return False
                    # 遍历完一页数据后记录剩余个数
                    total_query_nums -= page_size
                # 遍历最后一页数据
                for rows in range(1,total_query_nums+1):
                    if query_division_code_condition not in self.Tu.get_data(rows, 4):
                        return False
                return True




if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eb = ExaminationPlaceBusiness(driver)

    sleep(3)
