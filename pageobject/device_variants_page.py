from utils.locator_loader import get_locator


class DeviceVariantsPage:

    def __init__(self, page, data):
        self.page = page
        self.data = data

    def configure_device(self):

        self.select_new_customer()

        self.select_colour()

        self.select_capacity()

        if self.data["planpicker"] == "prebuilt":

            self.select_contract()

            self.choose_device_plan()

            self.continue_without_tradein()

        elif self.data["planpicker"] == "build":

            self.click_build_your_plan()

            self.continue_without_tradein()

            self.select_contract()

            self.click_continue()

    def select_new_customer(self):

        popup = self.page.locator(
            get_locator(
                "device_variants_page",
                "new_customer"
            )
        )

        if popup.is_visible():
            popup.click()

    def select_colour(self):

        if self.data.get("colour"):

            self.page.get_by_text(
                self.data["colour"]
            ).click()

    def select_capacity(self):

        if self.data.get("capacity"):

            self.page.get_by_text(
                self.data["capacity"]
            ).click()

    def click_build_your_plan(self):

        self.page.locator(
            get_locator(
                "device_variants_page",
                "build_your_plan"
            )
        ).click()

    def select_contract(self):

        if self.data.get("contract") == "24":

            self.page.locator(
                get_locator(
                    "device_variants_page",
                    "contract_24"
                )
            ).click()

    def choose_device_plan(self):

        selected_plan = (
            self.page
            .locator(
                get_locator(
                    "device_variants_page",
                    "device_plan_card"
                )
            )
            .filter(
                has_text=self.data["planname"]
            )
        )

        selected_plan.get_by_role(
            "button",
            name="Choose Plan"
        ).click()

    def continue_without_tradein(self):

        popup = self.page.locator(
            get_locator(
                "device_variants_page",
                "continue_without_tradein"
            )

        )

        if popup.is_visible():

            popup.click()

    def click_continue(self):

        self.page.locator(
            get_locator(
                "device_variants_page",
                "continue_btn"
            )
        ).click()