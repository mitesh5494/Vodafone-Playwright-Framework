from playwright.sync_api import Page

from pageobject.base_page import BasePage


class AddressPage(
    BasePage
):

    PAGE = "address_page"

    def __init__(
            self,
            page: Page,
            data
    ):

        super().__init__(
            page
        )

        self.data = data

    def bbl_view_broadband_plans(self):



        self.page.get_by_role(
            "combobox"
        ).select_option(
            self.data["housenum"]
        )

        self.click(
            "new_land_radio_btn"
        )

        self.click(
            "recently_moved_radio_btn"
        )

        self.click(
            "view_broadband_plans_btn"
        )