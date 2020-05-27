#import HTMLTestRunner
from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
import unittest
from case.examination_place_add_ddt_case import ExaminationPlaceAddDdtCase
from case.examination_place_edit_ddt_case import ExaminationPlaceEditDdtCase
from case.examination_place_delete_ddt_case import ExaminationPlaceDeleteDdtCase
from case.examination_place_query_ddt_case import ExaminationPlaceQueryDdtCase


class ExaminationPlace():
    def suite(self):
        # 一次性加载一个类文件下所有测试用例到suite中去。
        examinnation_place_add = unittest.makeSuite(ExaminationPlaceAddDdtCase)
        examination_place_edit = unittest.makeSuite(ExaminationPlaceEditDdtCase)
        examination_place_delete = unittest.makeSuite(ExaminationPlaceDeleteDdtCase)
        examination_place_query = unittest.makeSuite(ExaminationPlaceQueryDdtCase)
        return examination_place_edit, examinnation_place_add, examination_place_delete,examination_place_query


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    EX = ExaminationPlace()
    S = EX.suite()

    fire_path = r"D:\pythonWork\autoTest\report\examination_place.html"
    f = open(fire_path, 'wb')
    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',description=u'这是我们添加考点删除考点测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考点管理测试报告', description='考点管理的添加，编辑，删除，查询测试报告测试用例执行结果如下：')
    run = HTMLTestRunner()
    for i in range(0, S.__len__()):
        runner.run(S[i])
