from httprunner import HttpRunner, Config, Step, RunRequest


class delect_section(HttpRunner):
    config = (
        Config("删除子部门")

            # 域名
            .base_url("${rand_yaml_data(host)}")

            # 用来决定是否验证服务器TLS证书的开关
            .verify(False)

            # 导出的变量
            .export(*[])
    )

    teststeps = [
        Step(
            RunRequest("get with params")

                .with_variables(
                **{
                    "id": "${rand_yaml_data(subdivision_id)}",
                }
            )
                # 请求路径
                .get("/cgi-bin/department/delete")

                # 请求参数
                .with_params(**{"access_token": "${rand_yaml_data(access_token)}", 'id': "$id"})

                # 请求头
                .with_headers(**{"User-Agent": "PostmanRuntime/7.26.10", "Content-Type": "application/json"})

                # .extract()
                #     .with_jmespath("body.access_token", "access_tonken")
                .validate()

                # 断言
                .assert_equal("status_code", 200)
                .assert_equal("body.errcode", 0)
                .assert_equal("body.errmsg", 'deleted')
        ), ]


if __name__ == "__main__":
    delect_section().test_start()
    pass
