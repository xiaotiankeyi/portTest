import os
import sys
sys.path.append(os.path.join(os.getcwd(), "pytest_api"))

from public import *
from config import *

class TestqueryProductDetail(object):
    
    def test_queryProductDetail(base_url):
        request_body = rand_json_apidata(file=os.path.join(testapi_data_path, "queryProductDetail.json"))
        print(request_body)
        # req = RunMain()
        # req.run_main(url=base_url + "/queryProductDetail", method="post")

if __name__ == "__main__":
    pytest.main(["-v", "-s"])
