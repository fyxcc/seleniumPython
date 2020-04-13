# coding=utf-8
'''
(1)拿到操作值, 是否执行
(2)拿到执行方法
(3)拿到输入数据
(4)是否有输入数据
有输入数据
     执行方法（输入数据，操作元素）
没有输入数据
      执行方法（操作元素）
(5)对比预期结果和实际结果的值
   对比结果一样，测试结论为pass；否则为fail
'''

from util.excel_util import ExcelUtil
from keyword_modal.examination_place__add_keyword import ExaminationPlaceAddKeyword
from selenium import webdriver


class ExaminationPlaceAddKeywordCases(object):
    # 执行关键词测试用例

    def run_keyword_excel_cases(self):
        self.Ek = ExaminationPlaceAddKeyword()
        self.excel_path = r'D:\pythonWork\autoTest\data\ExaninationPlaceAddKeyWord.xls'
        handle_excel = ExcelUtil(self.excel_path)
        # 获取 excel 关键词测试用例的条数
        cases_numbers = handle_excel.get_lines()
        actual_case_numbers = int(cases_numbers) - 1
        print("注册页获取到的关键词测试的测试用例条数为：%d" % actual_case_numbers)

        # 循环行数遍历测试用例
        if cases_numbers:
            # 第 0 行是标题行不作为用例执行
            for i in range(1, cases_numbers):
                # 获取测试用例的名称
                testcase_name = handle_excel.get_col_value(i, 0)
                # 获取用例是否执行
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == 'yes':
                    # 执行方法
                    keyword_method = handle_excel.get_col_value(i, 4)
                    # 输入数据
                    send_value = handle_excel.get_col_value(i, 5)
                    # 操作元素
                    operator_element = handle_excel.get_col_value(i, 6)
                    # 获得预期结果的方法
                    except_result_method = handle_excel.get_col_value(i, 7)
                    # 预期结果的值
                    except_result = handle_excel.get_col_value(i, 8)
                    # 实际结果
                    actual_result = handle_excel.get_col_value(i, 9)
                    # 反射：通过excel中的字符串执行python文件中的方法
                    self.run_keyword_method(keyword_method, operator_element, send_value)

                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_keyword_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                                print('第 %s 条用例执行预期结果，用例名称是: [%s]' % (i, testcase_name))
                            else:
                                handle_excel.write_value(i, 'fail')
                                print('第 %s 条用例执行预期结果，用例名称是: [%s]' % (i, testcase_name))
                        elif except_value[0] == 'element':
                            result = self.run_keyword_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                                print('第 %s 条用例执行预期结果，用例名称是: [%s]' % (i, testcase_name))
                            else:
                                handle_excel.write_value(i, 'fail')
                                print('第 %s 条用例执行预期结果，用例名称是: [%s]' % (i, testcase_name))
                        else:
                            print('没有else')


                    else:
                        print('第 %s 条用例不执行，用例名称是: [%s]，无预期结果' % (i, testcase_name))
        else:
            print("略略略~，请检查你是否有写测试用例！")

    # 执行关键字测试方法
    def run_keyword_method(self, keyword_method, operator_element='', send_value=''):

        print('keyword_method --->', keyword_method)
        print("operator_element --->", operator_element)
        print("send_value --->", send_value)
        # 反射机制
        execute_method = getattr(self.Ek, keyword_method)
        if operator_element == '' and send_value != '':
            result = execute_method(send_value)
        elif operator_element != '' and send_value == '':
            result = execute_method(operator_element)
        elif operator_element == '' and send_value == '':
            result = execute_method()
        else:
            result = execute_method(operator_element, send_value)
        return result

    # 获取预期结果的值
    def get_except_result_value(self, data):
        return data.split('=')


if __name__ == "__main__":
    lkc = ExaminationPlaceAddKeywordCases()
    lkc.run_keyword_excel_cases()

    # rkc.run_keyword_method('open_browser', '', 'chrome')
    # rkc.run_keyword_method('get_url', '', 'http://www.5itest.cn/register')
    # rkc.run_keyword_method('send_element_key', 'register_email', '123')
