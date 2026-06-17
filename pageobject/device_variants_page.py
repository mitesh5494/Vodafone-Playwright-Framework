from playwright.sync_api import Page
from utils.locator_loader import get_locator


class DeviceVariantsPage:

    def __init__(self, page: Page, data):
        self.page = page
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

    def select_colour(self):

        if self.data.get("colour"):
            dropdown = self.page.locator(get_locator("device_variants_page", "select_colour_dropdown"))
            dropdown.wait_for(state="visible")
            dropdown.click()
            self.page.get_by_role("option", name=self.data["colour"]).click()

    def select_capacity(self):

        if self.data.get("capacity"):
            dropdown = self.page.locator(get_locator("device_variants_page", "select_capacity_dropdown"))
            dropdown.wait_for(state="visible")
            dropdown.click()
            self.page.get_by_role("option", name=self.data["capacity"]).click()

    def click_build_your_plan(self):

        self.page.get_by_role("button",name=get_locator("device_variants_page", "build_your_plan")).click()

    def select_contract(self):

        if self.data.get("contract") == "24":
            btn = self.page.get_by_label(get_locator("device_variants_page", "contract_24"), exact=True)
            btn.wait_for(state="visible")
            btn.click()


    def choose_device_plan(self):

        selected_plan = self.page.locator(get_locator("device_variants_page", "device_plan_card")).filter(
            has=self.page.get_by_text(self.data["deviceplandata"], exact=True))
        selected_plan.wait_for(state="visible")
        selected_plan.get_by_role("button", name="Choose these plans").click()

    def continue_without_tradein(self):

        popup = self.page.get_by_text(get_locator("device_variants_page", "continue_without_tradein"),exact=True)
        popup.wait_for(state="visible")
        popup.click()

    def click_continue(self):

        continuebtn = self.page.get_by_text(get_locator("device_variants_page", "continue_btn"))
        continuebtn.wait_for(state="visible")
        continuebtn.click()
