#import HTMLTestRunner
import sys

from util.htmltestrunner.HTMLTestRunner import HTMLTestRunner
#from util.HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
sys.path.append('D:/pythonWork/autoTest')
from case.examination_room_basic_info_edit import ExaminationRoomBasicInfoEditDdtCase
from case.examination_room_basic_select_ddt_case import ExaminationRoomBasicSelectDdtCase
from case.examination_room_traffic_info_edit import ExaminationRoomTrafficInfoEditDdtCase
from case.examination_room_book_add_ddt_case import ExaminationRoomBookAddDdtCase
from case.examination_room_book_delete_ddt_case import ExaminationRoomBookDeleteDdtCase
from case.examination_room_book_edit_ddt_case import ExaminationRoomBookEditDdtCase
class ExaminationRoom():
    def suite(self):
        # 一次性加载一个类文件下所有测试用例到suite中去。
        examination_room_basic_info_edit= unittest.makeSuite(ExaminationRoomBasicInfoEditDdtCase)
        examination_room_basic_select = unittest.makeSuite(ExaminationRoomBasicSelectDdtCase)
        examination_room_traffic_info_edit = unittest.makeSuite(ExaminationRoomTrafficInfoEditDdtCase)
        examination_room_book_add = unittest.makeSuite(ExaminationRoomBookAddDdtCase)
        examination_room_book_delete = unittest.makeSuite(ExaminationRoomBookDeleteDdtCase)
        examination_room_book_edit = unittest.makeSuite(ExaminationRoomBookEditDdtCase)
        return examination_room_basic_info_edit, examination_room_basic_select, examination_room_traffic_info_edit,examination_room_book_add,examination_room_book_delete,examination_room_book_edit


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    EX = ExaminationRoom()
    S = EX.suite()

    fire_path = r"D:\pythonWork\autoTest\report\examination_room.html"
    f = open(fire_path, 'wb')
    # 测试结果以报告显示
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='考点测试套件执行结果报告',description=u'这是我们考点基本资料的基本资料，交通路线，通讯录的测试报告',verbosity=2)
    runner = HTMLTestRunner(stream=f, title='考场管理测试报告', description='考点基本资料的基本资料，交通路线，通讯录测试用例执行结果如下：')
    for i in range(0, S.__len__()):
        runner.run(S[i])