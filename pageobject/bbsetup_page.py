from playwright.sync_api import Page

from pageobject.base_page import BasePage


class BBSetupPage(BasePage):
    PAGE = "setup_page"

    def __init__(self, page: Page, report=None):
        super().__init__(page, report)

    def continue_to_basket_page(self):
        print(self.nth("line_info", 0).text_content())

        self.check("bill_payer_checkbox")

        self.select("date_dropdown", index=1)

        self.check("digital_voice_checkbox")

        self.check_and_capture("telecare_checkbox", "telecare_checked")

        self.page.get_by_role("button", name="Go to basket").click()

        self.wait()

        self.capture("go_to_basket")
