from playwright.sync_api import Page, expect
from utils.locator_loader import get_locator


class BasePage:

    PAGE = None

    def __init__(self, page: Page, report=None):

        self.page = page
        self.report = report

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

    def locator_value(self, locator_name, page=None):

        return get_locator(
            page or self.PAGE,
            locator_name
        )

    def capture(self, screenshot_name):

        if self.report:

            self.report.capture(
                self.page,
                f"{self.PAGE}_{screenshot_name}"
            )

    def wait(
            self,
            state="domcontentloaded",
            timeout=15000
    ):

        self.page.wait_for_load_state(
            state,
            timeout=timeout
        )

    def click(self, locator_name):

        self.locator(
            locator_name
        ).click()

    def click_first(self, locator_name):

        self.locator(
            locator_name
        ).first.click()

    def fill(self, locator_name, value):

        self.locator(
            locator_name
        ).fill(
            value
        )

    def check(self, locator_name):

        self.locator(
            locator_name
        ).check()

    def select(self, locator_name, **kwargs):

        self.locator(
            locator_name
        ).select_option(
            **kwargs
        )

    # ==========================
    # Wrapper Methods
    # ==========================

    def click_and_capture(
            self,
            locator_name,
            screenshot_name=None,
            wait=True,
            wait_state="domcontentloaded"
    ):

        self.click(
            locator_name
        )

        if wait:

            self.wait(
                wait_state
            )

        self.capture(
            screenshot_name
            or locator_name
        )

    def click_first_and_capture(
            self,
            locator_name,
            screenshot_name=None,
            wait=True,
            wait_state="domcontentloaded"
    ):

        self.click_first(
            locator_name
        )

        if wait:

            self.wait(
                wait_state
            )

        self.capture(
            screenshot_name
            or locator_name
        )

    def fill_and_capture(
            self,
            locator_name,
            value,
            screenshot_name=None
    ):

        self.fill(
            locator_name,
            value
        )

        self.capture(
            screenshot_name
            or locator_name
        )

    def check_and_capture(
            self,
            locator_name,
            screenshot_name=None
    ):

        self.check(
            locator_name
        )

        self.capture(
            screenshot_name
            or locator_name
        )

    def select_and_capture(
            self,
            locator_name,
            screenshot_name=None,
            **kwargs
    ):

        self.select(
            locator_name,
            **kwargs
        )

        self.capture(
            screenshot_name
            or locator_name
        )

    def text(self, locator_name):

        return (
            self.locator(
                locator_name
            )
            .inner_text()
        )

    def count(self, locator_name):

        return (
            self.locator(
                locator_name
            )
            .count()
        )

    def nth(self, locator_name, index):

        return (
            self.locator(
                locator_name
            )
            .nth(index)
        )

    def visible(self, locator_name):

        expect(
            self.locator(
                locator_name
            )
        ).to_be_visible()

    def enabled(self, locator_name):

        expect(
            self.locator(
                locator_name
            )
        ).to_be_enabled()