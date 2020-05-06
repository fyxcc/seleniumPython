# coding=utf-8
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import time
from case.login_keyword_cases import LoginKeywordCases
from handle.examination_place_handle import ExaminationPlaceHandle
from util.table_util import TableUtil


class ExaminationRoomHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.ERp = ExaminationRoomPage(self.driver)
        self.Tu = TableUtil(self.driver)

