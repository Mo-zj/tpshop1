import os, sys
sys.path.append(os.getcwd())

from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class LoginPage(BaseAction):

    # 点击我的
    mine_btn = By.XPATH, ["text,我的", "resource-id,com.tpshop.malls:id/tab_txtv,1"]
    # 点击登录
    login_singup_btn = By.XPATH, "text,登录/注册"
    # 定位用户名输入框
    username_textbox = By.XPATH, "text,请输入手机号码"
    # 定位密码输入框
    pwd_textbox = By.ID, "com.tpshop.malls:id/edit_password"
    # 定位登录按钮
    login_btn = By.ID, "com.tpshop.malls:id/btn_login"


    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击我的和登录/注册
        self.jump_2_login_page()

    def jump_2_login_page(self):
        self.click(self.mine_btn)
        self.click(self.login_singup_btn)

    def input_username(self, text):
        self.input_text(self.username_textbox, text)

    def input_pwd(self, text):
        self.input_text(self.pwd_textbox, text)

    def click_login(self):
        self.click(self.login_btn)









