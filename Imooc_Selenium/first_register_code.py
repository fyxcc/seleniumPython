# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from util import ShowapiRequest

# 打开页面


driver = webdriver.Chrome("E:\software\Application\chromedriver.exe")


# driver=webdriver.Firefox()

# 浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    # 最大化窗口
    driver.maximize_window()
    time.sleep(5)


# 获取element 信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element


# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456abcdefghigklmn', 5))
    return user_info


# 获取验证码图片
def get_code_image(file_name):
    # (1)将含有验证码的页面截图保存下来（这里指的是注册页面）
    driver.save_screenshot(file_name)
    # (2)定位图片验证码图片的坐标
    code_element = driver.find_element_by_id('getcode_num')
    # (3)计算图片四个定点的位置
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    image = Image.open(file_name)
    # (4)将图片验证截取
    code_image = image.crop((left, top, right, height))
    code_image.save(file_name)


# 解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "156943", "889229f1478e460883969df323f4865f")
    r.addBodyPara("typeId", "35")  # 5位验证码
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name)
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text


# 运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info + "@163.com"
    file_name = "E:/image/register_cody.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()


run_main()
