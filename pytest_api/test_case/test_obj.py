import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.getcwd(), "pytest_api"))
from public.base_module import logger

class TestProject(object):
    def test_01(self):
        logger.info("测试一")
        a = 3
        b = 4
        assert a != b

    @pytest.mark.div     # div为标记
    def test_02(self):
        logger.info("测试二")

    
    def test_03(self):
        a = 3
        b = 4
        assert a != b
        logger.info("测试三")

    def test_04(self):
        logger.info("测试四")


if __name__ == "__main__":
    path_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_obj.py")
    # -q 简化控制台输出
    # -v 详细执行信息
    # -s 输出调试信息
    # -k 执行关键字用例"-k","01"
    # -m 执行标记的用例"-m", "run_02"
    # -x 执行失败立即停止
    # --maxfail=n执行失败几次停止执行 "--maxfail", "2"
    # --reruns失败后重跑
    pytest.main([path_file, "-v", "-s", "-m", "div"])