from playwright.sync_api import Page

from utils.locator_loader import get_locator
from utils.test_data_loader import get_test_data


class PlansPage:
    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def prebuilt_plans(self):
        if self.data["planpicker"] == "prebuilt":
            self.page.locator(get_locator("plans_page","choose_a_plan")).click()

        selected_plan_card = self.page.locator(get_locator("plans_page", "prebuilt_plan_card")).filter(
            has=self.page.get_by_text(self.data["planname"], exact=True))
        selected_plan_card.get_by_role("button", name="Choose Plan").click()

    def build_a_plan(self):

        selected_speed_card = self.page.locator(get_locator("plans_page", "speed_card")).filter(
            has_text=self.data["speed"])

        selected_speed_card.get_by_role("button", name="Select").click()
        if self.data["plantype"] == "extra":
            self.page.locator(get_locator("plans_page","broadband_tv")).click()

        selected_plan_card = self.page.locator(get_locator("plans_page", "plan_card")).filter(
            has=self.page.get_by_text(self.data["planname"], exact=True))
        selected_plan_card.get_by_role("button", name="Choose Plan").click()
