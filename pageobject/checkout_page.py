from playwright.sync_api import Page, expect

from pageobject.base_page import BasePage


class CheckoutPage(BasePage):
    PAGE = "checkout_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def checkout(self):

        self.__fill_about_you()

        if self.data["product"] in ["broadband", "simo"]:

            self.__address_detail()

            self.continue_btn()

            self.__choose_your_delivery_address_and_continue_to_payment()

            self.__bank_acc_details_and_continue()

        elif self.data["product"] == "handset":

            self.__address_detail()

            self.continue_btn()

            self.__bank_acc_details_and_continue()

    def __fill_about_you(self):

        self.page.get_by_role("combobox", name="Who are you buying for today?").select_option(self.data["checkout_customer_type"])

        self.fill("email", self.data["checkout_email"])

        self.page.get_by_role("combobox", name="Title").select_option(self.data["checkout_customer_title"])

        self.fill("firstname", self.data["checkout_first_name"])

        self.fill("lastname", self.data["checkout_last_name"])

        self.fill("contact_num", self.data["checkout_contact_num"])

        self.page.get_by_role("combobox", name="Employment status").select_option(self.data["checkout_emp_status_dropdown"])

        self.page.get_by_placeholder("DD").fill(self.data["checkout_dd"])

        self.page.get_by_placeholder("MM").fill(self.data["checkout_mm"])

        self.page.get_by_placeholder("YYYY").fill(self.data["checkout_yyyy"])

        self.capture("about_you_completed")

        continue_btn = self.locator("continue_to_add_detail")

        expect(continue_btn).to_be_enabled(timeout=10000)

        continue_btn.click()

        self.wait()

    def __address_detail(self):

        self.page.get_by_label(self.locator_value("postcode")).fill(self.data["checkout_postcode"])

        search_btn = self.page.get_by_text(self.locator_value("search_add_btn"))

        expect(search_btn).to_be_enabled(timeout=10000)

        search_btn.click()

        self.page.get_by_role("combobox", name="Addresses found").select_option(self.data["checkout_address"])

        self.page.get_by_role("combobox", name="Residential status").select_option(self.data["Residential_status"])

        self.page.get_by_placeholder("MM").fill(self.data["Date_you_move_in_dd"])

        self.page.get_by_placeholder("YYYY").fill(self.data["Date_you_move_in_yyyy"])

        self.capture("address_completed")

    def continue_btn(self):

        continue_btn = self.page.get_by_text(self.locator_value("add_continue_btn"))

        expect(continue_btn).to_be_enabled(timeout=10000)

        continue_btn.click()

        self.wait()

        self.capture("address_continue")

    def __choose_your_delivery_address_and_continue_to_payment(self):

        if self.data["Checkout_delivery_add"] == "installation":

            self.page.get_by_role("radio", name="Installation address").check()

        else:

            self.page.get_by_role("button", name="Continue to Monthly payment panel").click()

        self.wait()

        self.capture("delivery_address_selected")

    def __bank_acc_details_and_continue(self):

        self.page.get_by_role("textbox", name="Account holder name").fill(self.data["checkout_account_holder_name"])

        self.page.get_by_label("Account number", exact=True).fill(self.data["checkout_account_number"])

        self.page.get_by_label("1 of 3").fill(self.data["checkout_sortcode1"])

        self.page.get_by_label("2 of 3").fill(self.data["checkout_sortcode2"])

        self.page.get_by_label("3 of 3").fill(self.data["checkout_sortcode3"])

        self.locator("checkout_checkbox_I_agree_to_the_Direct_Debit").check()

        self.capture("payment_details_completed")

        continue_btn = self.page.get_by_role("button", name="Continue")

        expect(continue_btn).to_be_enabled(timeout=10000)

        continue_btn.click()

        self.wait()

        self.capture("checkout_completed")
