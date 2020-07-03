# coding=utf-8
'''
@project : binocular_vision
@author  : Hoodie_Willi
#@description: $输出sift匹配后，匹配点的坐标
#@time   : 2019-05-28 10:25:36
'''
import numpy as np
import cv2
class ImageMatchBySift():
    def image_match_by_sift(self,function_photo,screen_capture):
            sift = cv2.xfeatures2d.SIFT_create()
            img1 = cv2.imread(function_photo, cv2.COLOR_BGR2GRAY)
            img2 = cv2.imread(screen_capture, cv2.COLOR_BGR2GRAY)
            kp1, des1 = sift.detectAndCompute(img1, None)
            kp2, des2 = sift.detectAndCompute(img2, None)
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)

            # ## Create flann matcher
            # FLANN_INDEX_KDTREE = 1 # bug: flann enums are missing
            # flann_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            # #matcher = cv2.FlannBasedMatcher_create()
            # matcher = cv2.FlannBasedMatcher(flann_params, {})

            ## Ratio test
            print(len(matches))
            result_left=0
            result_right=0
            count=0
            matchesMask = [[0, 0] for i in range(len(matches))]
            for i, (m1, m2) in enumerate(matches):
                if m1.distance < 0.7 * m2.distance:  # 两个特征向量之间的欧氏距离，越小表明匹配度越高。
                    matchesMask[i] = [1, 0]
                    pt1 = kp1[m1.queryIdx].pt  # trainIdx    是匹配之后所对应关键点的序号，第一个载入图片的匹配关键点序号
                    pt2 = kp2[m1.trainIdx].pt  # queryIdx  是匹配之后所对应关键点的序号，第二个载入图片的匹配关键点序号
                    # print(kpts1)
                    print(i, pt1, pt2)
                    result_left+=pt2[0]
                    result_right+=pt2[1]
                    count+=1
                    if i % 5 == 0:
                        cv2.circle(img1, (int(pt1[0]), int(pt1[1])), 5, (255, 0, 255), -1)
                        cv2.circle(img2, (int(pt2[0]), int(pt2[1])), 5, (255, 0, 255), -1)

            result_left=result_left/count
            result_right=result_right/count
            operate_location=(result_left,result_right)
            return operate_location


            # 匹配点为蓝点, 坏点为红点
            draw_params = dict(matchColor=(255, 0, 0),
                               singlePointColor=(0, 0, 255),
                               matchesMask=matchesMask,
                               flags=0)

            res = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
            cv2.imshow("Result", res)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
if __name__ == '__main__':
    function_photo = r'D:\pythonWork\autoTest\util\image_match_sift\function_photo\picturedemo.png'
    screen_capture = r'D:\pythonWork\autoTest\util\image_match_sift\screen_capture\o.png'
    IM = ImageMatchBySift()
    print(IM.image_match_by_sift(function_photo, screen_capture))