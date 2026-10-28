from playwright.sync_api import Page

from utils.config import config

class LoginPage:
    "登录页"
    
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")
        
    def open(self):
        """打开登录页"""
        self.page.goto(config.BASE_URL)
        return self
    
    def login(self,username: str,password: str):
        """执行登录操作"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self
    
    def get_error_text(self) -> str:
        return self.error_message.inner_text()
    
    def pause(self):
        self.page.pause()
        return
        
    

    