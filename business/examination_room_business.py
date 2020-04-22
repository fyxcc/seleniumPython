#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from handle.examination_room_handle import ExaminationRoomHandle
from util.table_util import TableUtil
from time import sleep


class ExaminationRoomBusiness(object):
    def __init__(self, driver):
        self.driver = driver
        self.ERh = ExaminationRoomHandle(self.driver)
        self.Tu = TableUtil(self.driver)

    # 判断详情页面元素是否完整
    def judge_page_complete(self):
        if self.ERh.judge_basic_info() and self.ERh.judge_traffic_info() and self.ERh.judge_book_info():
            return True
        else:
            return False

if __name__ == "__main__":
    lkc = LoginKeywordCases()
    lkc.run_keyword_excel_cases()
    driver = getattr(getattr(lkc, 'lk'), 'driver')
    driver.maximize_window()
    EPh = ExaminationPlaceHandle(driver)
    EPh.click_detailed_btn()
    ERb = ExaminationRoomBusiness(driver)
    sleep(2)
    print(ERb.judge_page_complete())