import time

from playwright.sync_api import Page, expect
from pygments.lexers import data
from pytest_playwright.pytest_playwright import page

from utils.locator_loader import get_locator
from utils.test_data_loader import get_test_data


class AddonPage:
    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def __plan_validation(self):
        # plan =self.page.locator(get_locator("addon_page","addon_plan"))
        # expect(plan).to_have_text(self.data["planname"])
        plan = self.page.get_by_text(self.data["planname"], exact=True)
        expect(plan).to_have_text(self.data["planname"])

    def select_hbb_addon(self):
        self.__plan_validation()
        add_on_cards = self.page.locator(get_locator("addon_page", "addons")).filter(has_text=self.data["addon"], )
        add_on_cards.get_by_role("button", name="Add").click()
        expect(
            add_on_cards.get_by_role("button", name="Selected")
        ).to_be_visible(timeout=10000)

    def continue_to_setup_page(self):
        self.page.locator(".sc-iIvHqT.eTiIgX").text_content()
        self.page.get_by_role("button", name="Continue").click()

    def select_handset_addon(self):
        if self.data.get("handset_addon"):
            handset_addon_acce_watch_card = self.page.locator(
                get_locator("addon_page", "handset_addon_acce_watch_card"))
            handset_addon = handset_addon_acce_watch_card.filter(
                has=self.page.get_by_text(self.data["handset_addon"], exact=True))
            handset_addon.get_by_role("button", name="Add to Basket").click()
        btn = self.page.locator(get_locator("addon_page", "addon_popup")).get_by_role("button", name="Add to Basket")
        btn.wait_for(state="visible")
        btn.click()
        self.basket_summary_continue_btn()

    def basket_summary_continue_btn(self):
        btn = self.page.locator(get_locator("sticky_basket", "basket_summary_continue_btn"))
        btn.wait_for(state="visible")
        btn.click()
