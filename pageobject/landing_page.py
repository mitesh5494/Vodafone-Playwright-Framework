from playwright.sync_api import Page

from utils.locator_loader import get_locator


class LandingPage:

    def __init__(self, page:Page):
        self.page = page

    def accept_cookies(self):
        btn = self.page.locator("#onetrust-accept-btn-handler")
        if btn.count() > 0:
           btn.click()

    def enter_postcode(self, postcode):
        self.page.locator(
            get_locator("landing_page", "postcode")
        ).fill(postcode)

    def click_check_availability(self):
        self.page.locator(
            get_locator("landing_page", "check_availability")
        ).first.click()
