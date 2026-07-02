from playwright.sync_api import Page

from pageobject.base_page import BasePage


class LandingPage(BasePage):
    PAGE = "landing_page"

    def __init__(self, page: Page, data, report=None):
        super().__init__(page, report)

        self.data = data

    def accept_cookies(self):
        self.locator("accept_cookies").wait_for(state="visible")

        self.click("accept_cookies")

    def __enter_postcode(self):
        self.fill("postcode", self.data["postcode"])

    def check_availability(self):
        self.__enter_postcode()

        self.click_first_and_capture("check_availability", "availability_clicked")
