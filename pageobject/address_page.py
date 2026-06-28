from playwright.sync_api import Page

from pageobject.base_page import BasePage


class AddressPage(BasePage):
    PAGE = "address_page"

    def __init__(self, page: Page, data, report=None):
        super().__init__(page, report)

        self.data = data

    def bbl_view_broadband_plans(self):
        self.page.get_by_role("combobox").select_option(self.data["housenum"])

        self.capture("address_selected")

        self.click("new_land_radio_btn")

        self.click_and_capture("recently_moved_radio_btn", "recently_moved_selected", wait=False)

        self.click_and_capture("view_broadband_plans_btn", "view_broadband_plans")
