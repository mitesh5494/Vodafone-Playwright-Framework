from playwright.sync_api import Page

from pageobject.base_page import BasePage


class PhonePlanPage(BasePage):
    PAGE = "phoneplan_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def select_contract(self):

        if self.data["planpicker"] == "build":
            self.select_custom_contract()

    def select_custom_contract(self):

        target_contract = int(self.data.get("contract"))

        if target_contract == 24:

            self.page.get_by_label("Min 24 months", exact=True).click()

            self.capture("contract_24_selected")

        elif 24 < target_contract < 36:

            tenure_minus_btn = (self.page.get_by_role("button", name=self.locator_value("tenure_minus_btn")))

            tenure_locator = (self.page.locator(self.locator_value("tenure_picker")))

            while True:

                current_tenure = (tenure_locator.text_content().strip())

                current_value = int(current_tenure.split()[0])

                if current_value == target_contract:
                    break

                tenure_minus_btn.click()

                self.page.wait_for_timeout(300)

            self.capture(f"contract_{target_contract}_selected")

        continue_btn = (self.page.locator(self.locator_value("continue_btn")))

        continue_btn.wait_for(state="visible")

        continue_btn.click()

        self.wait()

        self.capture("continue")
