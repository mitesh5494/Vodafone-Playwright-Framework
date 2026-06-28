from playwright.sync_api import Page

from pageobject.base_page import BasePage


class PlansPage(BasePage):
    PAGE = "plans_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def select_plan(self):

        product = (self.data["product"].lower())

        actions = {"broadband": self.select_broadband, "simo": self.select_simo, "handset": self.select_handset}

        actions[product]()

    def select_broadband(self):

        if self.data["planpicker"] == "prebuilt":
            self.click_and_capture("choose_a_plan", "choose_a_plan", wait=False)

            selected_plan_card = (self.locator("prebuilt_plan_card").filter(has=self.page.get_by_text(self.data["planname"], exact=True)))

            selected_plan_card.get_by_role("button", name="Choose Plan").click()

            self.wait()

            self.capture("prebuilt_plan_selected")

            return

        selected_speed_card = (self.locator("speed_card").filter(has_text=self.data["speed"]))

        selected_speed_card.get_by_role("button", name="Select").click()

        self.capture("speed_selected")

        if self.data.get("plantype") == "extra":
            self.click_and_capture("broadband_tv", "tv_selected", wait=False)

        selected_plan_card = (self.locator("broadband_plan_card").filter(has=self.page.get_by_text(self.data["planname"], exact=True)))

        selected_plan_card.get_by_role("button", name="Choose Plan").click()

        self.wait()

        self.capture("broadband_plan_selected")

    def select_simo(self):

        selected_plan = (self.locator("simo_plan_card").filter(has=self.page.get_by_text(self.data["planname"], exact=True)).first)

        selected_plan.wait_for(state="visible")

        selected_plan.get_by_role("button", name="Choose Plan").click()

        self.wait()

        self.capture("simo_plan_selected")

    def select_handset(self):

        device = (self.locator("device_card").filter(has=self.page.get_by_text(self.data["device_name"], exact=True)))

        device.wait_for(state="visible")

        device.first.click()

        self.wait()

        self.capture("device_selected")
