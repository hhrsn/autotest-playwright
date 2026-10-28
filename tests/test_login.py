import pytest

def test_login_success(login_page):
    """ 用例：标准用户登录成功"""
    
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in login_page.page.url, f"登录失败，当前URL{page.url}"
    
    title = login_page.page.locator("[data-test='title']").inner_text()
    assert title == "Products", f"页面标题不符，实际是：{title}"
    login_page.pause()
   
def test_login_locked_user(login_page):
    """用例：锁定用户登录失败，应停留在登录页"""
    login_page.login("locked_out_user", "secret_sauce")
    
    assert login_page.error_message.is_visible(),"错误提示没有出现"
    
    error_text = login_page.get_error_text()
    assert "Sorry" in error_text,f"错误提示不符，实际是：{error_text}"
    
    assert "inventory.html" not in login_page.page.url
    
@pytest.mark.parametrize(
    "username,password,should_succeed",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("problem_user", "secret_sauce", True),
        ("standard_user", "wrong_password", False),
    ],
    ids=["标准用户", "锁定用户", "问题用户", "错误密码"],
)

def test_login_matrix(login_page,username,password,should_succeed):
    login_page.login(username,password)
    
    if should_succeed:
        title = login_page.page.locator("[data-test='title']").inner_text()
        assert title == "Products", f"页面标题不符，实际是：{title}"
    else:
        assert login_page.error_message.is_visible()