from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from utils.test_data_loader import get_test_data


class AddonPage:
    data = get_test_data("FTTP_TC_Acq")
    def __init__(self,page:Page):
        self.page = page


    def continue_to_setup_page(self):
        self.page.get_by_role("button", name="Continue").click()

    def select_addon(self):
        add_on_cards=self.page.locator("div[class='sc-fOOuSg hZjsvN']").filter(has_text=self.data["addon"],)
        add_on_cards.get_by_role("button", name="Add").click()

