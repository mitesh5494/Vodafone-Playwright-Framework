from playwright.sync_api import Page

from pageobject.base_page import BasePage


class BBSetupPage(BasePage):
    PAGE = "setup_page"

    def __init__(self, page: Page, data, report=None):
        super().__init__(page, report)
        self.data = data

    def continue_to_basket_page(self):
        print(self.nth("line_info", 0).text_content())

        self.check("bill_payer_checkbox")

        self.select("date_dropdown", index=1)
        if self.data.get("plan") == "HBB":
            self.check("digital_voice_checkbox")

        self.check_and_capture("telecare_checkbox", "telecare_checked")

        self.page.get_by_role("button", name="Continue to basket").click()

        self.wait()

        self.capture("go_to_basket")
