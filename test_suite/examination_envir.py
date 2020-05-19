import HTMLTestRunner
import unittest
from case.examination_envir_ddt_case import ExaminationEnvirDdtCase
from case.examination_machine_ddt_case import ExaminationMachineDdtCase
from case.examination_photo_ddt_case import ExaminationPhotoDdtCase
3
class ExaminationRoom():
    def suite(self):
        # 一次性加载一个类文件下所有测试用例到suite中去。
        examination_envir= unittest.makeSuite(ExaminationEnvirDdtCase)
        examination_machine = unittest.makeSuite(ExaminationMachineDdtCase)
        examination_photo = unittest.makeSuite(ExaminationPhotoDdtCase)
        return examination_envir, examination_machine, examination_photo

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    EX = ExaminationRoom()
    S = EX.suite()

    fire_path = r"D:\pythonWork\autoTest\report\examination_envir.html"
    f = open(fire_path, 'wb')
    # 测试结果以报告显示
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='this is the first ddt report',
                                           description=u'这是我们考点环境的基本资料，机器设备，考点照片的测试报告',
                                           verbosity=2)
    for i in range(0, S.__len__()):
        runner.run(S[i])