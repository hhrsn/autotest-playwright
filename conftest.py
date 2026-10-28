import pytest
from utils.config import config
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pathlib import Path


@pytest.fixture
def login_page(page: Page) -> Page:
    """
    提供一个已打开登录页的page
    """
    lp = LoginPage(page)
    lp.open()
    return lp

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    """
    提供一个“已登录成功”的page供不测登录、但需要登录态的业务用例使用
    """
    lp = LoginPage(page)
    lp.open()
    lp.login(config.STANDARD_USER, config.PASSWORD)
    
    page.wait_for_url("**/inventory.html")
    return page

@pytest.fixture(scope="session")
def counter():
    print("\n>>> counter fixture 被创建了")
    yield 1
    print("\n>>> counter fixture 被销毁了")
    
    
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """把每条用例的执行结果记录到 item 上，供截图 fixture 判断成败"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(page, request):
    """用例失败时自动截图到 screenshots/ 目录"""
    yield
    # 下面是 yield 之后：用例已经跑完了
    if request.node.rep_call.failed:
        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)
        # 用例名做文件名，去掉 [ ] 这类特殊字符
        name = request.node.name.replace("[", "_").replace("]", "")
        page.screenshot(path=str(screenshot_dir / f"{name}.png"))

    
    
    
    
    