#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
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
        if assertText == '添加成功':
            result = self.Eh.get_add_success_text()
            if result=='添加成功':
                return True
            else:
                return False
        if len(assertCode) != 0:
            if self.Eh.get_user_text(assertCode, assertText) is None:
                return False
            else:
                print("用例通过")
                return True
        else:
            if assertText == '添加失败!':
                if self.Eh.judge_add_frame():
                    return True
                else:
                    return False
            elif assertText == '添加成功':
                if self.Eh.judge_add_frame():
                    return False
                elif self.result == assertText:
                    self.driver.refresh()
                    if place_code == self.get_last_table_data():
                        print('添加成功，用例通过')
                        return True
                    else:
                        return False

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
            self.Eh.send_query_place_division_code_child('fchild')
        elif way == 'schild':
            self.Eh.send_query_place_division_code_child('schild')
        else:
            self.Eh.send_query_place_division_code_child('tchild')

    # 验证行政区划查询结果是否正确
    def judge_query_result(self, col):
        # 获取输入查询条件
        if col == '4':
            query_condition = self.Eh.get_place_division_code_condition()
        elif col == '2':
            query_condition = self.Eh.get_query_code_condition()
        elif col == '3':
            query_condition = self.Eh.get_query_name_condition()

        # 点击查询按钮
        self.Eh.click_query_btn()
        # 获取table查询总数
        total_query_nums = self.Tu.get_lines()
        # 判断查询结果和table查询结果数目是否相等
        if self.Tu.get_lines() == self.Eh.get_query_result_count_text():
            # 当查询数据存储在一页的时候
            if self.Tu.judge_click_next_page() == 0:
                for rows in range(1, total_query_nums + 1):
                    # 判断对应字段字段是否包含查询条件内容
                    if query_condition not in self.Tu.get_data(rows, col):
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
                        if query_condition not in self.Tu.get_data(rows, col):
                            return False
                    # 遍历完一页数据后记录剩余个数
                    total_query_nums -= page_size
                    self.Tu.click_next_page()
                    #self.Tu.click_refresh_next_page()
                # 遍历最后一页数据
                for rows in range(1, total_query_nums + 1):
                    if query_condition not in self.Tu.get_data(rows, 4):
                        return False
                return True

    # 获取启用数量
    def get_enable_num(self):
        count = 0
        # 获取table查询总数
        total_query_nums = self.Tu.get_lines()
        # 判断查询结果和table查询结果数目是否相等
        if self.Tu.get_lines() == self.Eh.get_query_result_count_text():
            # 当查询数据存储在一页的时候
            if self.Tu.judge_click_next_page() == 0:
                for rows in range(1, total_query_nums + 1):
                    # 判断对应字段字段是否包含查询条件内容
                    if self.Tu.get_data(rows, '12') == '启用':
                        count += 1
            # 当查询结果分页保存的时候
            else:
                # 获取点击下一页次数
                click_next_page = self.Tu.judge_click_next_page()
                # 获取table每页行数
                page_size = self.Tu.get_page_size()
                for click_nums in range(1, click_next_page + 1):
                    for rows in range(1, page_size + 1):
                        if self.Tu.get_data(rows, '12') == '启用':
                            count += 1
                    # 遍历完一页数据后记录剩余个数
                    total_query_nums -= page_size
                    self.Tu.click_next_page()
                # 遍历最后一页数据
                for rows in range(1, total_query_nums + 1):
                    if self.Tu.get_data(rows, '12')=='启用':
                        count+=1
                return count
    # 清空输入条件
    def clear_query_condition(self):
        self.Eh.clear_query_condition()
        self.Eh.click_query_btn()

    # 输入查询条件
    def send_query_condition(self, query_code, query_name):
        self.Eh.send_query_place_code(query_code)
        self.Eh.send_query_place_name(query_name)

    # 查询功能数据驱动
    def query_function(self, query_code, query_name, col):
        if col == '未查询到相关记录':
            self.send_query_condition(query_code, query_name)
            self.Eh.click_query_btn()
            time.sleep(1)
            if self.Eh.get_empty_result_text() == '未查询到相关记录':
                result = True
                self.Eh.click_empty_result_btn()
            else:
                result = False
        else:
            self.send_query_condition(query_code, query_name)
            result = self.judge_query_result(col)
        return result

    # 判断信息列表是否默认按照考点编号正序排序
    def judge_orderby_seq(self, type, col):
        page_size = self.Tu.get_page_size()
        query_result_num = self.Eh.get_query_result_count_text()
        if page_size < query_result_num:
            size = page_size
        else:
            size = query_result_num
        if type == 'positive':
            for row in range(1, size):
                if len(self.Tu.get_data(row, col)) != 0 and len(self.Tu.get_data(row + 1, col)) != 0:
                    if col != '2':
                        if int(self.Tu.get_data(row, col)) > int(self.Tu.get_data(row + 1, col)):
                            return False
                    else:
                        if self.Tu.get_data(row, col) > self.Tu.get_data(row + 1, col):
                            return False
        elif type == 'inverted':
            for row in range(1, size):
                if len(self.Tu.get_data(row, col)) != 0 and len(self.Tu.get_data(row + 1, col)) != 0:
                    if col != '2':
                        if int(self.Tu.get_data(row, col)) < int(self.Tu.get_data(row + 1, col)):
                            return False
                    else:
                        if self.Tu.get_data(row, col) < self.Tu.get_data(row + 1, col):
                            return False
        return True

    # 判断信息列表是否支持按照考点编号正序、倒序排序
    def judge_code_order(self, type):
        if type == 'code_positive':
            self.Eh.click_table_code_positive_seq()
            result = self.judge_orderby_seq('positive', '2')
        elif type == 'code_inverted':
            self.Eh.click_table_code_inverted_seq()
            result = self.judge_orderby_seq('inverted', '2')
        elif type == 'exam_place_num_positive':
            self.Eh.click_exam_place_num_positive_seq()
            result = self.judge_orderby_seq('positive', '8')
        elif type == 'exam_place_num_inverted':
            self.Eh.click_exam_place_num_inverted_seq()
            result = self.judge_orderby_seq('inverted', '8')
        elif type == 'use_computer_num_positive':
            self.Eh.click_use_computer_num_positive_seq()
            result = self.judge_orderby_seq('positive', '9')
        elif type == 'use_computer_num_inverted':
            self.Eh.click_use_computer_num_inverted_seq()
            result = self.judge_orderby_seq('inverted', '9')
        elif type == 'table_total_computer_num_positive':
            self.Eh.click_table_total_computer_num_positive_seq()
            result = self.judge_orderby_seq('positive', '10')
        elif type == 'table_total_computer_num_inverted':
            self.Eh.click_table_total_computer_num_inverted_seq()
            result = self.judge_orderby_seq('inverted', '10')
        return result

    # 获取列表最后一行数据
    def get_last_table_data(self):
        rows = self.Tu.get_lines() % self.Tu.get_page_size()
        click_num = self.Tu.judge_click_next_page()
        for i in range(1, click_num + 1):
            self.Tu.click_refresh_next_page()
        code_data = self.Tu.get_data(rows, '2')
        return code_data

    # 判断是否点击详情跳转考场管理页面
    def judge_detailed_btn(self):
        self.Eh.click_detailed_btn()
        time.sleep(1)
        current_url=self.driver.current_url
        if current_url=='http://localhost:9090/exam-place/examinationRoom':
            return True
        else:
            return False


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eb = ExaminationPlaceBusiness(driver)
    print(Eb.get_enable_num())
    sleep(3)
