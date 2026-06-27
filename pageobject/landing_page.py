from playwright.sync_api import Page

from pageobject.base_page import BasePage


class LandingPage(BasePage):

    PAGE = "landing_page"

    def __init__(
            self,
            page: Page,
            data
    ):

        super().__init__(page)

        self.data = data

    def accept_cookies(self):

        self.locator("accept_cookies").wait_for(state="visible")

        self.click("accept_cookies")

    def enter_postcode(self):

        self.fill(
            "postcode",
            self.data["postcode"]
        )

    def click_check_availability(self):


        self.locator(
            "check_availability"
        ).first.click()