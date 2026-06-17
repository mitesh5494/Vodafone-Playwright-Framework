from playwright.sync_api import Page
from utils.locator_loader import get_locator


class PhonePlanPage:

    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def select_contract(self):
        if self.data["planpicker"] == "build":
            self.select_custom_contract()


    def select_custom_contract(self):

        target_contract = int(self.data.get("contract"))

        if target_contract == 24:
            self.page.get_by_label("Min 24 months", exact=True).click()

        elif 24 < target_contract < 36:

            tenure_minus_btn = self.page.get_by_role("button", name=get_locator("phoneplan_page", "tenure_minus_btn"))

            tenure_locator = self.page.locator(get_locator("phoneplan_page", "tenure_picker"))

            while True:
                current_tenure = tenure_locator.text_content().strip()

                # Example: "30 months" → 30
                current_value = int(current_tenure.split()[0])

                if current_value == target_contract:
                    break

                tenure_minus_btn.click()

                self.page.wait_for_timeout(300)


        continue_btn=self.page.locator(get_locator("phoneplan_page","continue_btn"))
        continue_btn.wait_for(state="visible")
        continue_btn.click()





