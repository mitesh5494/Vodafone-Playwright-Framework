from playwright.sync_api import Page, expect

from pageobject.base_page import BasePage
from utils.locator_loader import get_locator


class AddonPage(BasePage):
    PAGE = "addon_page"

    def __init__(self, page: Page, data, report=None):
        super().__init__(page, report)

        self.data = data

    def plan_validation(self):
        plan = self.page.get_by_text(self.data["planname"], exact=True)

        expect(plan).to_have_text(self.data["planname"])

    def select_hbb_addon(self):
        self.plan_validation()

        add_on_cards = (self.locator("addons").filter(has_text=self.data["addon"]))

        add_on_cards.get_by_role("button", name="Add").click()

        expect(add_on_cards.get_by_role("button", name="Selected")).to_be_visible(timeout=10000)

        self.capture("addon_selected")

    def continue_to_setup_page(self):

        bb_plan_name=self.text_content("bb_plan_name")
        assert bb_plan_name == self.data["planname"]

        self.page.get_by_role("button", name="Continue").click()

        self.wait()

        self.capture("continue_to_setup")

    def select_handset_addon(self):
        if self.data.get("handset_addon"):
            handset_addon = (self.locator("handset_addon_acce_watch_card").filter(has=self.page.get_by_text(self.data["handset_addon"], exact=True)))

            handset_addon.get_by_role("button", name="Add to Basket").click()

            self.capture("handset_addon_selected")

        btn = (self.locator("addon_popup").get_by_role("button", name="Add to Basket"))

        btn.wait_for(state="visible")

        btn.click()

        self.capture("addon_popup_confirmed")

        self.basket_summary_continue_btn()

    def basket_summary_continue_btn(self):
        btn = (self.page.locator(self.locator_value("basket_summary_continue_btn", page="sticky_basket")))

        btn.wait_for(state="visible")

        btn.click()

        self.wait()

        self.capture("basket_summary_continue")
