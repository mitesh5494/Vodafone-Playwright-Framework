import time

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from utils.locator_loader import get_locator
from utils.test_data_loader import get_test_data


class AddonPage:
    def __init__(self, page: Page, data):
        self.page = page
        self.data = data


    def continue_to_setup_page(self):
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)

    def select_addon(self):
        add_on_cards=self.page.locator(get_locator("addon_page","addons")).filter(has_text=self.data["addon"],)
        add_on_cards.get_by_role("button", name="Add").click()
        expect(
            add_on_cards.get_by_role("button", name="Selected")
        ).to_be_visible(timeout=10000)


