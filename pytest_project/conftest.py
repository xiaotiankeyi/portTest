# import os
# import pytest
# # 项目目录配置
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# REPORT_DIR = BASE_DIR + "/test_report/"

# ############################

# # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。

# # 配置运行的 URL
# url = "http://127.0.0.1:7777"

# # 失败重跑次数
# rerun = "2"

# # 当达到最大失败数，停止执行
# max_fail = "5"

# # 运行测试用例的目录或文件
# cases_path = "./testcases/"

# ############################


# # 定义基本测试环境
# @pytest.fixture(scope='function')
# def base_url():
#     global url
#     return url


# # 设置用例描述表头
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('Time', class_='sortable time', col='time'))
#     cells.insert(2, html.th('Description'))
#     cells.pop()


# # 设置用例描述表格
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = description_html(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         report.extra = extra


# def description_html(desc):
#     """
#     将用例中的描述转成HTML对象
#     :param desc: 描述
#     :return:
#     """
#     if desc is None:
#         return "No case description"
#     desc_ = ""
#     for i in range(len(desc)):
#         if i == 0:
#             pass
#         elif desc[i] == '\n':
#             desc_ = desc_ + ";"
#         else:
#             desc_ = desc_ + desc[i]

#     desc_lines = desc_.split(";")
#     desc_html = html.html(
#         html.head(
#             html.meta(name="Content-Type", value="text/html; charset=latin1")),
#         html.body(
#             [html.p(line) for line in desc_lines]))
#     return desc_html

# def new_report_time():
#     """
#     获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
#     """
#     files = os.listdir(REPORT_DIR)
#     files.sort()
#     try:
#         return files[-1]
#     except IndexError:
#         return None

# if __name__ == "__main__":
#     pass