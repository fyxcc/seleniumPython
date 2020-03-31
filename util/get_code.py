# coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
from basic.find_element import FindElement


class GetCode:
    # 构造方法
    def __init__(self, driver):
        self.driver = driver

    # 定位用户信息，获取元素element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取验证码图片
    def get_captcha_image(self, file_name):
        self.driver.save_screenshot(file_name)
        captcha_element = self.get_user_element('login_getcode_num')
        left = captcha_element.location['x']
        top = captcha_element.location['y']
        right = captcha_element.size['width'] + left
        height = captcha_element.size['height'] + top
        image = Image.open(file_name)
        img = image.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

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
        time.sleep(2)
        return text
