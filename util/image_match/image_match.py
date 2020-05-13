import cv2
import numpy as np
from matplotlib import pyplot as plt


class ImageMatch():
    def ImageMatch(self, function_photo, screen_capture):
        # 读取原图
        img = cv2.imread(screen_capture, 0)
        img2 = img.copy()
        # 读取模板图
        template = cv2.imread(function_photo, 0)
        # 记录图像模板的尺寸
        w, h = template.shape[::-1]
        # 六种模板匹配算法：平方差匹配法，归一化平方差匹配法，相关匹配法(最慢，运算量大)，归一化相关匹配法，相关系数匹配法，归一化相关系数匹配法
        methods = ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_CCOEFF',
                   'cv2.TM_CCOEFF_NORMED']
        for meth in methods:
            img = img2.copy()
            # eval 语句用来计算存储在字符串中的有效 Python 表达式
            method = eval(meth)
            # 模板匹配
            res = cv2.matchTemplate(img, template, method)
            # 寻找最值
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # 使用不同的比较方法，对结果的解释不同，如果方法是TM_SQDIFF或TM_SQDIFF_NORMED，则取最小值

            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            # 绘制矩形
            cv2.rectangle(img, top_left, bottom_right, 255, 2)
            plt.subplot(121), plt.imshow(res, cmap='gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(img, cmap='gray')
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()


if __name__ == '__main__':
    function_photo = r'D:\pythonWork/autoTest\util\image_match/function_photo\photo_file_path.png'
    screen_capture = r'D:\pythonWork/autoTest\util\image_match\screen_capture\photo_add.png'
    IM = ImageMatch()
    IM.ImageMatch(function_photo, screen_capture)
