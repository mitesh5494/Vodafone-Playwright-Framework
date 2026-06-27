from playwright.sync_api import Page, expect
from utils.locator_loader import get_locator


class BasePage:

    PAGE = None

    def __init__(self, page: Page):
        self.page = page

    def locator(self, locator_name):
        """
        Return Playwright locator
        Example:
        self.locator("continue_btn")
        """

        return self.page.locator(
            get_locator(
                self.PAGE,
                locator_name
            )
        )

    def click(self, locator_name):

        self.locator(
            locator_name
        ).click()

    def click_first(
            self,
            locator_name
    ):
        self.locator(
            locator_name
        ).first.click()

    def fill(
            self,
            locator_name,
            value
    ):

        self.locator(
            locator_name
        ).fill(value)

    def text(
            self,
            locator_name
    ):

        return (
            self.locator(
                locator_name
            )
            .inner_text()
        )

    def count(
            self,
            locator_name
    ):

        return (
            self.locator(
                locator_name
            )
            .count()
        )

    def nth(
            self,
            locator_name,
            index
    ):

        return (
            self.locator(
                locator_name
            )
            .nth(index)
        )

    def visible(
            self,
            locator_name
    ):

        expect(
            self.locator(
                locator_name
            )
        ).to_be_visible()

    def enabled(
            self,
            locator_name
    ):

        expect(
            self.locator(
                locator_name
            )
        ).to_be_enabled()

    def wait(self):

        self.page.wait_for_load_state(
            "networkidle"
        )