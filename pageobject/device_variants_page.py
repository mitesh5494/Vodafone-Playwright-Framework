from playwright.sync_api import Page

from pageobject.base_page import BasePage


class DeviceVariantsPage(BasePage):
    PAGE = "device_variants_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def configure_device(self):

        self.select_new_customer()

        self.select_colour()

        self.select_capacity()

        if self.data["planpicker"] == "prebuilt":

            self.select_contract()

            self.choose_device_plan()

            self.continue_without_tradein()

        elif self.data["planpicker"] == "build":

            self.click_build_your_plan()

            self.continue_without_tradein()

    def select_new_customer(self):

        popup = self.page.get_by_role("button", name="I'm a new customer")

        popup.wait_for(state="visible")

        popup.click()

        self.capture("new_customer_selected")

    def select_colour(self):

        if self.data.get("colour"):
            dropdown = self.locator("select_colour_dropdown")

            dropdown.wait_for(state="visible")

            dropdown.click()

            self.page.get_by_role("option", name=self.data["colour"]).click()

            self.capture("colour_selected")

    def select_capacity(self):

        if self.data.get("capacity"):
            dropdown = self.locator("select_capacity_dropdown")

            dropdown.wait_for(state="visible")

            dropdown.click()

            self.page.get_by_role("option", name=self.data["capacity"]).click()

            self.capture("capacity_selected")

    def click_build_your_plan(self):

        self.page.get_by_role("button", name=self.locator_value("build_your_plan")).click()
        self.wait()

        self.capture("build_your_plan")

    def select_contract(self):

        if self.data.get("contract") == "24":
            btn = (self.page.get_by_label(self.locator_value("contract_24"), exact=True))

            btn.wait_for(state="visible")

            btn.click()

            self.capture("contract_selected")

    def choose_device_plan(self):

        selected_plan = (self.locator("device_plan_card").filter(has=self.page.get_by_text(self.data["deviceplandata"], exact=True)))

        selected_plan.wait_for(state="visible")

        selected_plan.get_by_role("button", name="Choose these plans").click()

        self.wait()

        self.capture("device_plan_selected")

    def continue_without_tradein(self):

        popup = self.page.get_by_text(self.locator_value("continue_without_tradein"), exact=True)

        popup.wait_for(state="visible")

        popup.click()

        self.wait()

        self.capture("continue_without_tradein")

    def click_continue(self):

        continue_btn = self.page.get_by_text(self.locator_value("continue_btn"))

        continue_btn.wait_for(state="visible")

        continue_btn.click()

        self.wait()

        self.capture("continue")
