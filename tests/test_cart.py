from pages.Inventory_page import InventoryPage
from playwright.sync_api import expect

def test_add_to_cart(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    assert inv.get_cart_count() == 1, f"角标显示 {inv.get_cart_count()}，预期 1"
    # logged_in_page.pause()
    
    
def test_remove_from_cart(logged_in_page):
    inv = InventoryPage(logged_in_page)
    inv.add_to_cart("sauce-labs-backpack")
    inv.add_to_cart("sauce-labs-bike-light")
    inv.remove_product("sauce-labs-backpack")
    
    inv.open_cart()
    assert "cart.html" in logged_in_page.url, f"当前不在购物车页：{logged_in_page.url}"
    page = logged_in_page
    
    #取所有匹配元素的文本返回列表
    # expect() 会自动重试（默认 5 秒），等页面真正加载完、数据真正到位
    expect(page.locator("[data-test='inventory-item-name']")).to_have_count(1,timeout=2000)

    expect(page.locator("[data-test='inventory-item-name']")).to_have_text(
        ["Sauce Labs Bike Light"],timeout=2000
    )
