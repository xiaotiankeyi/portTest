from httprunner import HttpRunner, Config, Step, RunRequest


class create_section(HttpRunner):
    config = (
        Config("创建子部门")

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
                    "name": "广州研发中心",
                    "name_en": "DRGZ",
                    "order": "1",
                    "parentid": "${rand_yaml_data(parentid)}"
                }
            )
                # 请求路径
                .post("/cgi-bin/department/create")

                # 请求参数
                .with_params(**{"access_token": "${rand_yaml_data(access_token)}"})
                .with_json({
                "id": "$id",  # 指定子部门id
                "name": "$name",
                "name_en": "$name_en",
                "order": "$order",  # 在父部门中的次序值
                "parentid": "$parentid"  # 父部门id
            })
                # 请求头
                .with_headers(**{"User-Agent": "PostmanRuntime/7.26.10", "Content-Type": "application/json"})

                # .extract()
                #     .with_jmespath("body.access_token", "access_tonken")
                .validate()

                # 断言
                .assert_equal("status_code", 200)
                .assert_equal("body.errcode", 0)
                .assert_equal("body.errmsg", 'created')
                .assert_equal("body.id", "$id")
        ), ]


if __name__ == "__main__":
    create_section().test_start()
    pass
