from playwright.sync_api import Page

from pageobject.base_page import BasePage


class BBSetupPage(BasePage):
    PAGE = "setup_page"

    def __init__(self, page: Page, report=None):
        super().__init__(page, report)

    def continue_to_basket_page(self):
        print(self.nth("line_info", 0).text_content())

        self.check_and_capture("bill_payer_checkbox", "bill_payer_checked")

        self.select_and_capture("date_dropdown", "installation_date_selected", index=1)

        self.check_and_capture("digital_voice_checkbox", "digital_voice_checked")

        self.check_and_capture("telecare_checkbox", "telecare_checked")

        self.page.get_by_role("button", name="Go to basket").click()

        self.wait()

        self.capture("go_to_basket")
