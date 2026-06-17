from playwright.sync_api import Page

from utils.locator_loader import get_locator


class AirtimePlansPage:

    def __init__(self, page:Page, data):
        self.page = page
        self.data = data

    def select_airtime_plan(self):
        plan_data_filter = self.page.locator(
        f"{get_locator('airtimeplan_page', 'plan_data_filter')}[value='{self.data['deviceplandata']}']")
        plan_data_filter.click()

        plan = self.page.locator(get_locator("airtimeplan_page", "airtime_plan_card")).filter(has=self.page.get_by_text(self.data["deviceplan"],exact=True))
        plan.wait_for(state="visible")
        plan.get_by_role("button", name="Choose Plan").click()


