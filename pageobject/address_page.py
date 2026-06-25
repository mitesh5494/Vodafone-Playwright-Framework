from playwright.sync_api import Page

from utils.locator_loader import get_locator
from utils.test_data_loader import get_test_data


class AddressPage:
    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def bbl_view_broadband_plans(self):
        self.page.get_by_role("combobox").select_option(self.data["housenum"])

        self.page.locator(get_locator("address_page", "new_land_radio_btn")).click()
        self.page.locator(get_locator("address_page", "recently_moved_radio_btn")).click()
        self.page.locator(get_locator("address_page", "view_broadband_plans_btn")).click()
