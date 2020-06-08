import os, sys, pytest, allure, time
sys.path.append(os.getcwd())

from base.base_yml import yaml_data_with_file
from base.base_driver import init_driver
from page.login_page import LoginPage


def data_with_key(key):
    return yaml_data_with_file("login_data", key)


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = LoginPage(self.driver)

    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):

        username = args["username"]
        pwd = args["password"]
        toast = args["toast"]
        # 截图的名字
        screen_name = args["screen_name"]

        # 1.点击我的, 点击登录/注册

        # 2.输入用户名
        allure.attach("输入用户名" + username, "")
        self.login_page.input_uername(username)

        # 3.输入密码
        allure.attach("输入密码" + pwd, "")
        self.login_page.input_pwd(pwd)

        # 4.点击登录
        allure.attach("点击登录", "")
        self.login_page.click_login()

        allure.attach("判断对应的提示是否正确", toast)
        res = self.login_page.is_toast_exist(toast, True, screen_name)
        time.sleep(1)

        # 使用allure上传图片
        allure.attach("登录截图", open('./screen/'+ screen_name +'.png', 'rb').read(), allure.attach_type.PNG)

        # 5.根据toast断言成功或者失败
        assert self.login_page.is_toast_exist(toast)









