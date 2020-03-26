# coding=utf-8
from selenium import webdriver
from time import sleep

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from util.read_ini import ReadIni
from basic.find_element import FindElement
import random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Register(object):
    def __init__(self, url, i):
        self.driver = self.get_driver(url, i)

    # 启动浏览器，打开目标测试页面url
    def get_driver(self, url, i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 定位用户信息，获取元素element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 获取随机数
    def get_range(self):
        number = ''.join(random.sample('abcdefg123456', 8))
        return number

    # 获取验证码图片
    def get_captcha_image(self, file_name):
        self.driver.save_screenshot(file_name)
        captcha_element = self.get_user_element('getcode_num')
        left = captcha_element.location['x']
        top = captcha_element.location['y']
        right = captcha_element.size['width'] + left
        height = captcha_element.size['height'] + top
        image = Image.open(file_name)
        img = image.crop((left, top, right, height))
        img.save(file_name)

    # 识别图片验证码
    def discern_captcha_image(self, file_name):
        self.get_captcha_image(file_name)
        # 解析验证码图片中的文字（用第三方的图片验证码识别接口 ShowApiRequest）
        r = ShowapiRequest("http://route.showapi.com/184-4", "156943", "889229f1478e460883969df323f4865f")
        r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text

    # 主函数
    def main(self):
        register_nickname = self.get_range()
        register_email = self.get_range() + '@163.com'
        register_password = self.get_range() + '@123'
        file_name = '../image/code_image.png'
        captcha_code = self.discern_captcha_image(file_name)
        self.send_user_info('register_nickname', register_nickname)
        self.send_user_info('register_email', register_email)
        self.send_user_info('register_password', register_password)
        self.send_user_info('captcha_code', 111111)
        self.get_user_element('register_btn').click()
        captcha_code_error = self.get_user_element('captcha_code_error')
        if captcha_code_error is None:
            print("......恭喜你注册成功了......")
        else:
            self.driver.save_screenshot('../image/captcha_code_error.png')
        sleep(5)
        self.driver.close()


if __name__ == "__main__":
    # for i in range(3):
    register_url = 'http://www.5itest.cn/register'
    r = Register(register_url, 2)
    r.main()
