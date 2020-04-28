# coding=utf-8
from faulthandler import is_enabled

from selenium.webdriver import ActionChains

from basic.find_element import FindElement

from case.login_keyword_cases import LoginKeywordCases


class TableUtil:
    def __init__(self, driver, table_path=None):
        self.driver = driver
        self.fe = FindElement(driver)
        if table_path is None:
            self.table_path = 'query_table'
            self.table = self.fe.get_element(self.table_path, 'ExaminationPlacePage')
        else:
            self.table_path = table_path
            self.table=self.fe.get_element(self.table_path, 'ExaminationPlaceRoom')

    #  获取单元格的数据(行号与列号）
    def get_data(self, row=0, col=0):
        if self.get_lines() >= row:
            data_xpath = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div[1]/div[2]/table/tbody' + '/tr[' + str(
                row) + ']/td[' + str(col) + ']'
            data = self.driver.find_element_by_xpath(data_xpath).text
            return data
        return None
    #  获取单元格的数据(行号与列号）
    def get_data_book(self, row=0, col=0):
        data_xpath = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[5]/div/div/div[1]/div[2]/table/tbody/tr ' + '/td[' + str(col) + ']'
        data = self.driver.find_element_by_xpath(data_xpath)
        if data!=None:
            return data.text
        else:
            return None

    # 获取table总行数
    def get_lines(self):
        # 行数
        total_numbers_xpath = 'query_table_total_numbers'
        numbers_string = self.fe.get_element(total_numbers_xpath, 'ExaminationPlacePage').text
        numbers_list = numbers_string.split(' ')
        rows = int(numbers_list[1])
        if rows >= 1:
            return rows
        return None

    # 获取table每页行数
    def get_page_size(self):
        page_size = 'page_size'
        size_string = self.fe.get_element(page_size, 'ExaminationPlacePage').text
        size_list = size_string.split(' ')
        size = int(size_list[0])
        return size

    # 点击下一页
    def click_next_page(self):
        next_page_btn = self.fe.get_element('next_page_btn', 'ExaminationPlacePage')
        next_page_btn.click()

    # 点击刷新的下一页

    def click_refresh_next_page(self):
        next_page_btn = self.fe.get_element('refresh_next_page_btn', 'ExaminationPlacePage')
        next_page_btn.click()

    # 点击下一页次数
    def judge_click_next_page(self):
        page_size = self.get_page_size()
        query_total_lines = self.get_lines()
        count = int(query_total_lines / page_size)
        return count


if __name__ == '__main__':
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    tu = TableUtil(driver)
    print(tu.get_enable_num())
