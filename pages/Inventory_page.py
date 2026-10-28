from playwright.sync_api import Page

class InventoryPage:
    "商品页"
    def __init__(self,page:Page):
        self.page = page
        #页面固定元素
        self.title = page.locator("[data-test='title']")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
    
    def add_to_cart(self,product_name:str):
        btn = self.page.locator(f"[data-test='add-to-cart-{product_name}']")
        btn.click()
        return self
    
    def remove_product(self,product_name:str):
        btn = self.page.locator(f"[data-test='remove-{product_name}']")
        btn.click()
        return self
    
    def open_cart(self):
        self.cart_link.click()
        return self

    def get_title(self) -> str:
        return self.title.inner_text()
    
    def get_cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())