from pytest_project.public.base_module import *


class Testlogin(startup):

    @pytest.mark.parametrize('value', rand_yaml_data(file=api_data_path,))
    def test_case_01(self, value, base_url):
        headers = value['request']['headers']
        url = value['request']['url']
        data = value['request']['json']
        data = json.dumps(data)
        method = value['request']['method']

        response = RunMain()
        response = response.run_main(url=base_url+url, method=method, headers=headers, data=data)
        print(response)

        assert value['validate']['equal'] == response['msg']
        logger.info("{}请求,响应body{}".format(url, response))

    case_data = rand_excel()
    @pytest.mark.parametrize(
        'casenumber,'
        ' testitem, testfunction, YN, Host, URLPath, Method, RequestDataType, RequestData, test_assert, remark',
        case_data)
    def test_case_02(
        self,
        base_url,
        casenumber,
        testitem,
        testfunction,
        YN,
        Host,
        URLPath,
        Method,
        RequestDataType,
        RequestData,
        test_assert,
        remark,
    ):

        headers = eval(RequestDataType)
        url = URLPath
        data = RequestData
        data = eval(json.dumps(data))
        print('参数', data)
        method = Method
        text_assret = eval(test_assert)
        # print(text_assret['msg'])

        response = RunMain()
        response = response.run_main(
            url=base_url + url,
            method=method,
            headers=headers,
            data=data)
        print(response)

        assert text_assret['msg'] == response['msg']
        assert text_assret['msg_code'] == response['msg_code']

    pass


if __name__ == "__main__":
    pytest.main(['-vs', '-q', 'test_Userlogin.py::Testlogin::test_case_01', '--html=report.html'])
    # pytest.main(['-vs', 'test_Userlogin.py::Testlogin::test_case_02', '--alluredir', 'report'])
    # os.system('allure generate --clean report/ -o report_result/html')
