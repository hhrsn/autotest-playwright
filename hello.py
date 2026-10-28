from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000)
    page = browser.new_page()
    
    page.goto("https://www.saucedemo.com")
    
    page.locator("[data-test='username']").fill("standard_user")
    
    page.locator("[data-test='password']").fill("secret_sauce")
    
    page.locator("[data-test='login-button']").click()
    
    assert "inventory.html" in page.url, f"登录失败，当前URL{page.url}"
    print("登录成功")
        
    print("当前页面 URL:", page.url)
    
    input("按回车键关闭浏览器...") 