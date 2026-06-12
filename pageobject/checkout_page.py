from playwright.sync_api import Page, expect

from utils.locator_loader import get_locator
from utils.test_data_loader import get_test_data


class CheckoutPage:
    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def fill_about_you(self):
        self.page.get_by_role(
            "combobox",
            name="Who are you buying for today?"
        ).select_option(self.data["checkout_customer_type"])

        self.page.locator(
            get_locator("checkout_page", "email")
        ).fill(self.data["checkout_email"])

        self.page.get_by_role(
            "combobox",
            name="Title"
        ).select_option(self.data["checkout_customer_title"])

        self.page.locator(
            get_locator("checkout_page", "firstname")
        ).fill(self.data["checkout_first_name"])

        self.page.locator(
            get_locator("checkout_page", "lastname")
        ).fill(self.data["checkout_last_name"])

        self.page.locator(
            get_locator("checkout_page", "contact_num")
        ).fill(self.data["checkout_contact_num"])

        self.page.get_by_role(
            "combobox",
            name="Employment status"
        ).select_option(self.data["checkout_emp_status_dropdown"])

        self.page.get_by_placeholder("DD").fill(
            self.data["checkout_dd"]
        )

        self.page.get_by_placeholder("MM").fill(
            self.data["checkout_mm"]
        )

        self.page.get_by_placeholder("YYYY").fill(
            self.data["checkout_yyyy"]
        )

    def continue_to_add_detail(self):
        continue_to_add_detail = self.page.locator(get_locator("checkout_page", "continue_to_add_detail"))
        expect(continue_to_add_detail).to_be_enabled(timeout=10000)
        continue_to_add_detail.click()

    def address_detail(self):
        self.page.get_by_label(get_locator("checkout_page", "postcode")).fill(self.data["checkout_postcode"])
        search_postcode=self.page.get_by_text(get_locator("checkout_page", "search_add_btn"))
        expect(search_postcode).to_be_enabled(timeout=10000)
        search_postcode.click()
        self.page.get_by_role("combobox", name="Addresses found").select_option(self.data["checkout_address"])
        self.page.get_by_role("combobox", name="Residential status").select_option(self.data["Residential_status"])
        self.page.get_by_placeholder("MM").fill(self.data["Date_you_move_in_dd"])
        self.page.get_by_placeholder("YYYY").fill(self.data["Date_you_move_in_yyyy"])

    def continue_to_broadband(self):
        continue_btn = self.page.get_by_text(get_locator("checkout_page", "add_continue_btn"))
        expect(continue_btn).to_be_enabled(timeout=10000)
        continue_btn.click()


