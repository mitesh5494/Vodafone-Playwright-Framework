from playwright.sync_api import Page

from pageobject.base_page import BasePage


class AirtimePlansPage(BasePage):
    PAGE = "airtimeplan_page"

    def __init__(self, page: Page, data, report=None):
        super().__init__(page, report)

        self.data = data

    def select_airtime_plan(self):
        plan_data_filter = self.page.locator(f"{self.locator_value('plan_data_filter')}[value='{self.data['deviceplandata']}']")

        plan_data_filter.click()


        self.capture("plan_data_filter_selected")

        plan = (self.locator("airtime_plan_card").filter(has=self.page.get_by_text(self.data["deviceplan"], exact=True)))

        plan.wait_for(state="visible")

        plan.get_by_role("button", name="Choose Plan").click()

        self.wait()

        self.capture("plan_selected")
