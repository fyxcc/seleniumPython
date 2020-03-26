# coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "156943", "889229f1478e460883969df323f4865f")
r.addBodyPara("typeId", "35")#5位验证码
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", "E:/immoc1.png")
res = r.post()
text = res.json()["showapi_res_body"]["Result"]

print(text)  # 返回信息
print(res.text)
