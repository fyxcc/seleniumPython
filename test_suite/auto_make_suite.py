import HTMLTestRunner
import unittest
from util.excel_util import ExcelUtil
from case.examination_envir_ddt_case import ExaminationEnvirDdtCase
from case.examination_machine_ddt_case import ExaminationMachineDdtCase
from case.examination_photo_ddt_case import ExaminationPhotoDdtCase
# 获取数据
ex = ExcelUtil(excel_path=r"D:\pythonWork\autoTest\data\automakesuite.xls")


class AutoMakeSuite():
    def make_suite(self):
        # 获取列表测试用例个数
        l1 = ex.get_data()
        rows=ex.get_lines()
        result=[]
        for i in range(0,rows):
            a = eval(ex.get_col_value(i,2))
            examination= unittest.makeSuite(a)
            result.append(examination)
        return result

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    AMS= AutoMakeSuite()
    MS=AMS.make_suite()
    fire_path = r"D:\pythonWork\autoTest\report\auto_make_suite.html"
    f = open(fire_path, 'wb')
    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们考点环境的基本资料，机器设备，考点照片的测试报告',
                                           verbosity=2)
    length=len(MS)
    for i in range(0, length):
        runner.run(MS[i])

