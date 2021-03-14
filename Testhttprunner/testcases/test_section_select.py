from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from Testhttprunner.testcases.test_access_token import access_token


class find_section(HttpRunner):
    config = (
        Config("获取部门列表")

            # 域名
            .base_url(rand_yaml_data(key='host'))

            # 用来决定是否验证服务器TLS证书的开关
            .verify(False)

            # 导出的变量
            .export(*[])
    )

    teststeps = [
        Step(
            RunTestCase("导入access")
                .call(access_token)
                .export(*['access_tonken'])
        ),
        Step(
            RunRequest("get with params")

                # 适用于当前步骤的参数
                # .with_variables(
                # **{"foo1": "bar11", "foo2": "bar21", }
            # )

                # 请求路径
                .get("/cgi-bin/department/list")

                # 请求参数
                .with_params(**{"access_token": rand_yaml_data(key='access_token')})

                # 请求头
                .with_headers(**{"User-Agent": "PostmanRuntime/7.26.10"})

                # .extract()
                #     .with_jmespath("body.access_token", "access_tonken")
                .validate()

                # 断言
                .assert_equal("status_code", 200)
                .assert_equal("body.errcode", 0)
                .assert_equal("body.errmsg", 'ok')
        ), ]


if __name__ == "__main__":
    find_section().test_start()
    pass
