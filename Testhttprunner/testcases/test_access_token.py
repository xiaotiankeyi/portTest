from httprunner import HttpRunner, Config, Step, RunRequest

class access_token(HttpRunner):
    """
    获取access_token值
    """

    # 公共配置
    config = (
        Config("获取access_token值")

            # 公共参数所有步骤都可调用`
        #     .variables(
        #     **{
        #
        #     }
        # )
            # 域名
            # .base_url(rand_yaml_data(key='host'))
            .base_url("${rand_yaml_data(host)}")

            # 用来决定是否验证服务器TLS证书的开关
            .verify(False)

            # 导出的变量
            .export(*["access_tonken"])
    )

    teststeps = [
        Step(
            RunRequest("get with params")

                # 适用于当前步骤的参数
                # .with_variables(
                # **{"foo1": "bar11", "foo2": "bar21", }
            # )

                # 请求路径
                .get("/cgi-bin/gettoken")

                # 请求参数
                .with_params(**{"corpid": "${rand_yaml_data(corpid)}", "corpsecret": "${rand_yaml_data(corpsecret)}"})

                # 请求头
                .with_headers(**{"User-Agent": "PostmanRuntime/7.26.10"})

                # 提取access_token值
                .extract()
                .with_jmespath("body.access_token", "access_tonken")
                .validate()
                # 断言
                .assert_equal("status_code", 200)
                .assert_equal("body.errcode", 0)
                .assert_equal("body.errmsg", 'ok')
                .assert_equal("body.expires_in", 7200)
        ), ]

if __name__ == "__main__":
    access_token().test_start()
    pass
