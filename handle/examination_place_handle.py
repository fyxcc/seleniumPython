# coding=utf-8
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from page.examination_place_page import ExaminationPlacePage
import time
from case.login_keyword_cases import LoginKeywordCases


class ExaminationPlaceHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.Ep = ExaminationPlacePage(self.driver)

    # 获取添加错误信息
    def get_user_text(self, error_info, assertText):
        try:

            if error_info == 'place_code_error':
                text_content = self.Ep.get_place_code_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_name_error':
                # text = self.Ep.get_place_name_error().text
                text_content = self.Ep.get_place_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_division_code_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                # text = self.Ep.get_place_division_code_error().text
                text_content = self.Ep.get_place_division_code_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_address_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.Ep.get_place_address_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_person_error':
                # text = self.Ep.get_place_person_error().text
                text_content = self.Ep.get_place_person_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'place_person_tel_error':
                # text = self.Ep.get_place_person_tel_error().text
                text_content = self.Ep.get_place_person_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.Ep.get_place_code_error().get_attribute("innerHTML")
                text2 = self.Ep.get_place_name_error().get_attribute("innerHTML")
                text3 = self.Ep.get_place_division_code_error().get_attribute("innerHTML")
                text4 = self.Ep.get_place_address_error().get_attribute("innerHTML")
                text5 = self.Ep.get_place_person_error().get_attribute("innerHTML")
                text6 = self.Ep.get_place_person_tel_error().get_attribute("innerHTML")
                if text1 and text2 and text3 and text4 and text5 and text6:
                    text = 'ok'

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 获取编辑错误信息

    def get_edit_user_text(self, error_info, assertText):
        try:

            if error_info == 'edit_place_code_error':
                text_content = self.Ep.get_edit_place_code_error().text
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_name_error':
                # text = self.Ep.get_edit_place_name_error().text
                text_content = self.Ep.get_edit_place_name_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_division_code_error':
                '''
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[3]/div/div'))
                text = self.driver.find_element_by_xpath('/html/body/div[3]/div/div').text
                '''
                # text = self.Ep.get_place_division_code_error().text
                text_content = self.Ep.get_edit_place_division_code_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_address_error':
                # text = self.Ep.get_place_address_error().text
                text_content = self.Ep.get_edit_place_address_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_person_error':
                # text = self.Ep.get_edit_place_person_error().text
                text_content = self.Ep.get_edit_place_person_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'edit_place_person_tel_error':
                # text = self.Ep.get_edit_place_person_tel_error().text
                text_content = self.Ep.get_edit_place_person_tel_error().get_attribute("innerHTML")
                if text_content == assertText:
                    text = 'ok'
            elif error_info == 'repeat_place_code_error':
                WebDriverWait(self.driver, 10).until(
                    lambda x: x.find_element_by_xpath('/html/body/div[17]/div/div'))
                text_content = self.driver.find_element_by_xpath('/html/body/div[17]/div/div').text
                # text_content = self.Ep.get_edit_repeat_code_error().text
                if text_content == assertText:
                    text = 'ok'
            else:
                text1 = self.Ep.get_edit_place_code_error().get_attribute("innerHTML")
                text2 = self.Ep.get_edit_place_name_error().get_attribute("innerHTML")
                # text3 = self.Ep.get_edit_place_division_code_error().get_attribute("innerHTML")
                text4 = self.Ep.get_edit_place_address_error().get_attribute("innerHTML")
                text5 = self.Ep.get_edit_place_person_error().get_attribute("innerHTML")
                text6 = self.Ep.get_edit_place_person_tel_error().get_attribute("innerHTML")
                if text1 and text2 and text4 and text5 and text6:
                    text = 'ok'

            return text
        except BaseException as e:
            print(repr(e))
            return None

    # 输入考点编号
    def send_place_code(self, place_code):
        if place_code is not None:
            # value = str(place_code)
            self.Ep.get_place_code().send_keys(place_code)

    # 输入考点名称
    def send_place_name(self, place_name):
        if place_name is not None:
            self.Ep.get_place_name().send_keys(place_name)

    # 输入行政区划
    def send_place_division_code(self):
        self.Ep.get_place_division_code().click()
        self.Ep.get_place_division_code_fchild().click()
        time.sleep(1)
        self.Ep.get_place_division_code_schild().click()
        time.sleep(1)
        self.Ep.get_place_division_code_tchild().click()

    # 输入考点地址
    def send_place_address(self, place_address):
        if place_address is not None:
            self.Ep.get_place_address().send_keys(place_address)

    # 输入考点负责人
    def send_place_person(self, place_person):
        if place_person is not None:
            self.Ep.get_place_person().send_keys(place_person)

    # 输入负责人联系电话
    def send_place_person_tel(self, place_person_tel):
        if place_person_tel is not None:
            self.Ep.get_place_person_tel().send_keys(place_person_tel)

    # 选择状态
    def select_place_status(self):
        self.Ep.get_place_status().click()

    # 获取开关选择状态
    def get_place_status(self):
        # self.Ep.get_place_status_value().get_attribute('value')
        self.Ep.get_place_status_value()

    # 点击确定添加按钮
    def click_confirm_add_btn(self):
        self.Ep.get_confirm_add_btn().click()

    # 点击取消添加按钮
    def click_cancle_add_btn(self):
        self.Ep.get_cancle_add_btn().click()

    # 点击添加按钮
    def click_add_btn(self):
        self.Ep.get_add_btn().click()

    # 判断添加考点弹框是否打开
    def judge_add_frame(self):
        if self.Ep.get_add_frame() is not None:
            if self.Ep.get_add_frame().text == '添加考点':
                return True
        else:
            return False

    # 获取添加成功提示语
    def get_add_success_text(self):
        #time.sleep(2)
        return self.Ep.add_success().text

    # 点击删除考点按钮
    def click_delete_examination_place_btn(self):
        self.Ep.get_delete_examination_place_btn().click()

    # 判断删除考点弹框是否打开
    def judge_delete_frame(self):
        if self.Ep.get_delete_frame().text == '确定删除所选记录？':
            return True
        else:
            return False

    # 点击确认删除按钮
    def click_confirm_delete_btn(self):
        self.Ep.get_confirm_delete_btn().click()

    # 点击取消删除按钮
    def click_cancle_delete_btn(self):
        self.Ep.get_cancle_delete_btn().click()

    # 获得删除考点信息结果内容
    def get_delete_result(self):
        return self.Ep.get_delete_examination_place_result()

    # 输入编辑考点编号
    def send_edit_place_code(self, edit_place_code):
        if len(edit_place_code) != 0:
            # value = str(place_code)
            self.Ep.get_edit_place_code().send_keys(edit_place_code)

    # 输入编辑考点名称

    def send_edit_place_name(self, edit_place_name):
        if len(edit_place_name) != 0:
            self.Ep.get_edit_place_name().send_keys(edit_place_name)

    # 输入编辑行政区划

    def send_edit_place_division_code(self):
        self.Ep.get_edit_place_division_code().click()
        self.Ep.get_edit_place_division_code_fchild().click()
        time.sleep(1)
        self.Ep.get_edit_place_division_code_schild().click()
        time.sleep(1)
        self.Ep.get_edit_place_division_code_tchild().click()

    # 输入编辑考点地址

    def send_edit_place_address(self, edit_place_address):
        if len(edit_place_address) != 0:
            self.Ep.get_edit_place_address().send_keys(edit_place_address)

    # 输入编辑考点负责人

    def send_edit_place_person(self, edit_place_person):
        if len(edit_place_person) != 0:
            self.Ep.get_edit_place_person().send_keys(edit_place_person)

    # 输入编辑负责人联系电话

    def send_edit_place_person_tel(self, edit_place_person_tel):
        if len(edit_place_person_tel) != 0:
            self.Ep.get_edit_place_person_tel().send_keys(edit_place_person_tel)

    # 编辑选择状态

    def select_edit_place_status(self):
        self.Ep.get_edit_place_status().click()

    # 获取编辑开关选择状态

    def get_edit_place_status(self):
        # self.Ep.get_place_status_value().get_attribute('value')
        self.Ep.get_edit_place_status_value()

    # 点击编辑确定添加按钮

    def click_edit_confirm_btn(self):
        self.Ep.get_edit_confirm_btn().click()

    # 点击编辑取消添加按钮

    def click_edit_cancle_btn(self):
        self.Ep.get_edit_cancle_btn().click()

    # 点击编辑添加按钮

    def click_edit_btn(self):
        self.Ep.get_edit_btn().click()

    # 判断编辑考点弹框是否打开

    def judge_edit_frame(self):
        if self.Ep.get_edit_frame().text == '编辑考点':
            return True
        else:
            return False

    # 获取编辑成功提示语

    def get_edit_success_text(self):
        return self.Ep.get_edit_success().text

    # 获取回填数据
    def get_backfill_data(self):
        data1 = self.Ep.get_edit_place_code().get_attribute('value')
        print(data1)
        data2 = self.Ep.get_edit_place_name().get_attribute('value')
        print(data2)
        data3 = self.Ep.get_edit_place_division_code().get_attribute('value')
        print(data3)
        data4 = self.Ep.get_edit_place_address().get_attribute('value')
        print(data4)
        data5 = self.Ep.get_edit_place_person().get_attribute('value')
        print(data5)
        data6 = self.Ep.get_edit_place_person_tel().get_attribute('value')
        print(data6)
        if data1 and data2 and data3 and data4 and data5 and data6:
            result = '回填信息数据完整'
        else:
            result = '回填信息数据不完整'
        return result

    # 输入查询考点编号
    def send_query_place_code(self, query_place_code):
        if len(query_place_code) != 0:
            self.Ep.get_query_place_code().send_keys(query_place_code)

    # 清空查询条件
    def clear_query_condition(self):
        self.Ep.get_query_place_code().send_keys(Keys.CONTROL, 'a')
        self.Ep.get_query_place_code().send_keys(Keys.BACK_SPACE)
        self.Ep.get_query_place_name().send_keys(Keys.CONTROL, 'a')
        self.Ep.get_query_place_name().send_keys(Keys.BACK_SPACE)
        # self.Ep.get_query_place_division_code().send_keys(Keys.CONTROL, 'a')
        # self.Ep.get_query_place_division_code().send_keys(Keys.BACK_SPACE)
        # self.Ep.get_query_place_division_code().clear()

    # 点击行政区划取消按钮
    def click_clear_query_place_division_code_btn(self):
        cl = self.Ep.get_clear_query_place_division_code()
        ActionChains(self.driver).move_to_element(cl).perform()
        # self.Ep.get_clear_query_place_division_code().click()

    # 输入查询考点名称

    def send_query_place_name(self, query_place_name):
        if len(query_place_name) != 0:
            self.Ep.get_query_place_name().send_keys(query_place_name)

    # 输入查询一级行政区划
    def send_query_place_division_code_child(self, way):
        if way == 'fchild':
            self.Ep.get_query_place_division_code().click()
            self.Ep.get_query_place_division_code_fchild().click()
        elif way == 'schild':
            try:
                self.Ep.get_query_place_division_code().click()
                ActionChains(self.driver).move_to_element(self.Ep.get_query_place_division_code_fchild()).perform()
                self.Ep.get_query_place_division_code().click()
                ActionChains(self.driver).move_to_element(self.Ep.get_query_place_division_code_schild()).perform()
            except StaleElementReferenceException:
                self.Ep.get_query_place_division_code_schild().click()

        else:
            try:
                self.Ep.get_query_place_division_code().click()
                ActionChains(self.driver).move_to_element(self.Ep.get_query_place_division_code_fchild()).perform()
                self.Ep.get_query_place_division_code().click()
                ActionChains(self.driver).move_to_element(self.Ep.get_query_place_division_code_schild()).perform()
                self.Ep.get_query_place_division_code().click()
                ActionChains(self.driver).move_to_element(
                    self.Ep.get_query_place_division_code_tchild()).click().perform()
            except StaleElementReferenceException:
                self.Ep.get_query_place_division_code_tchild().click()

    # 点击查询按钮
    def click_query_btn(self):
        self.Ep.get_query_btn().click()

    # 获取总计数目项
    def get_query_total_count_text(self):
        return int(self.Ep.get_query_result_count().text)

    # 获取查询结果数目

    def get_query_result_count_text(self):
        return int(self.Ep.get_query_result_count().text)

    # 获取查询已选择数目

    def get_query_choiced_count_text(self):
        return int(self.Ep.get_choiced_count().text)

    # 清空按钮
    def click_clear_btn(self):
        self.Ep.get_clear_btn().click()

    # 获取查询条件行政区划内容
    def get_place_division_code_condition(self):
        content = self.Ep.get_query_place_division_code().get_attribute('value')
        if content.find('/'):
            content_list = content.split('/')
            result = content_list[0].strip() + '-'
            return result
        result = content
        return result

    # 获取查询条件考点编号内容：
    def get_query_code_condition(self):
        content = self.Ep.get_query_place_code().get_attribute('value')
        return content

    # 获取查询条件考点名称内容
    def get_query_name_condition(self):
        content = self.Ep.get_query_place_name().get_attribute('value')
        return content

    # 获取列表考点编号内容
    def get_table_place_code_text(self):
        return self.Ep.get_table_place_code().text

    # 获取列表考点名称内容
    def get_table_place_name_text(self):
        return self.Ep.get_table_place_name().text

    # 获取列表行政区划内容
    def get_table_place_division_code_text(self):
        return self.Ep.get_table_place_division_code().text

    # 获取列表考点地址内容
    def get_table_place_address_text(self):
        return self.Ep.get_table_place_address().text

    # 获取列表考点负责人内容
    def get_table_place_person_text(self):
        return self.Ep.get_table_place_person().text

    # 获取列表负责人联系电话内容
    def get_table_place_person_tel_text(self):
        return self.Ep.get_table_place_person_tel().text

    # 获取列表考场数内容

    def get_table_exam_place_num_text(self):
        return self.Ep.get_table_exam_place_num().text

    # 获取列表可编排机位数内容
    def get_table_use_computer_num_text(self):
        return self.Ep.get_table_use_computer_num().text

    # 获取列表总机位数内容

    def get_table_total_computer_num_text(self):
        return self.Ep.get_table_total_computer_num().text

    # 获取列表更新时间内容

    def get_table_update_time_text(self):
        return self.Ep.get_table_update_time().text

    # 获取列表状态内容
    def get_table_status_text(self):
        return self.Ep.get_table_status().text

    # 点击导出按钮
    def click_export_btn(self):
        self.Ep.get_export_btn().click()

    # 查询列表行政区划数据内容
    def get_query_place_division_code_data_text(self):
        return self.Ep.get_query_place_division_code_data().text

    # 判断查询条件是否完整：
    def judge_query_condition_complete(self):
        if self.Ep.get_query_place_code_placeholder() == '请输入考点编号' and self.Ep.get_query_place_name_placeholder() == '请输入考点名称' and self.Ep.get_query_place_division_code_placeholder() == '请选择':
            return True
        else:
            return False

    # 判断统计结果字段是否完整

    def judge_count_result_complete(self):
        if self.get_query_total_count_text() is not None and self.get_query_result_count_text() is not None and self.get_query_choiced_count_text() is not None:
            if self.Ep.get_clear_btn().text == '清空' and self.get_query_total_count_text() == self.get_query_result_count_text():

                return True
            else:
                return False
        else:
            return False

    # 判断信息列表是否完整
    def table_info_complete(self):
        col1 = self.get_table_place_code_text()
        col2 = self.get_table_place_name_text()
        col3 = self.get_table_place_division_code_text()
        col4 = self.get_table_place_address_text()
        col5 = self.get_table_place_person_text()
        col6 = self.get_table_place_person_tel_text()
        col7 = self.get_table_exam_place_num_text()
        col8 = self.get_table_use_computer_num_text()
        col9 = self.get_table_total_computer_num_text()
        col10 = self.get_table_update_time_text()
        col11 = self.get_table_status_text()
        if col1 == '考点编号' and col2 == '考点名称' and col3 == '行政区划' and col4 == '考点地址' and col5 == '考点负责人' and col6 == '负责人电话' and col7 == '考场数' and col8 == '可编排机位数' and col9 == '总机位数' and col10 == '更新时间' and col11 == '状态':
            return True
        else:
            return False

    # 判断按钮完整性
    def btn_complete(self):
        if self.Ep.get_query_btn().text == '查询' and self.Ep.get_add_btn().text == '+添加':
            return True
        else:
            return False

    # 未查询到结果弹框内容
    def get_empty_result_text(self):
        return self.Ep.get_empty_result().text

    # 点击确定未查询到结果弹框按钮

    def click_empty_result_btn(self):
        return self.Ep.get_empty_result_btn().click()

    # 点击考点编号正序按钮

    def click_table_code_positive_seq(self):
        return self.Ep.get_table_code_positive_seq().click()

    # 点击考点编号倒序按钮
    def click_table_code_inverted_seq(self):
        return self.Ep.get_table_code_inverted_seq().click()

    # 点击考场数正序按钮
    def click_exam_place_num_positive_seq(self):
        return self.Ep.get_exam_place_num_positive_seq().click()

    # 点击考场数倒序按钮
    def click_exam_place_num_inverted_seq(self):
        return self.Ep.get_exam_place_num_inverted_seq().click()

    # 点击可编排机位数正序按钮
    def click_use_computer_num_positive_seq(self):
        return self.Ep.get_use_computer_num_positive_seq().click()

    # 点击可编排机位数倒序按钮
    def click_use_computer_num_inverted_seq(self):
        return self.Ep.get_use_computer_num_inverted_seq().click()

    # 点击总机位数正序按钮
    def click_table_total_computer_num_positive_seq(self):
        return self.Ep.get_table_total_computer_num_positive_seq().click()

    # 点击总机位数倒序按钮
    def click_table_total_computer_num_inverted_seq(self):
        return self.Ep.get_table_total_computer_num_inverted_seq().click()
    #点击详情按钮
    def click_detailed_btn(self):
        return self.Ep.get_detailed_btn().click()


if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    Eh = ExaminationPlaceHandle(getattr(getattr(lkc, 'lk'), 'driver'))
    # Eh.send_query_place_code('999')
    # Eh.click_query_btn()
    # time.sleep(1)
    print(Eh.get_query_result_count_text())
    print(Eh.get_query_total_count_text())

    time.sleep(10)
