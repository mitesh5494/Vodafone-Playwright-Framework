from playwright.sync_api import Page
from utils.locator_loader import get_locator


class PlansPage:

    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def select_plan(self):

        product = self.data["product"].lower()

        actions = {
            "broadband": self.select_broadband,
            "simo": self.select_simo,
            "handset": self.select_handset
        }

        actions[product]()

    def select_broadband(self):

        if self.data["planpicker"] == "prebuilt":
            self.page.locator(
                get_locator(
                    "plans_page",
                    "choose_a_plan"
                )
            ).click()

            selected_plan_card = (
                self.page
                .locator(
                    get_locator(
                        "plans_page",
                        "prebuilt_plan_card"
                    )
                )
                .filter(
                    has=self.page.get_by_text(
                        self.data["planname"],
                        exact=True
                    )
                )
            )

            selected_plan_card.get_by_role(
                "button",
                name="Choose Plan"
            ).click()

            return

        selected_speed_card = (
            self.page
            .locator(
                get_locator(
                    "plans_page",
                    "speed_card"
                )
            )
            .filter(
                has_text=self.data["speed"]
            )
        )

        selected_speed_card.get_by_role(
            "button",
            name="Select"
        ).click()

        if self.data.get("plantype") == "extra":
            self.page.locator(
                get_locator(
                    "plans_page",
                    "broadband_tv"
                )
            ).click()

        selected_plan_card = (
            self.page
            .locator(
                get_locator(
                    "plans_page",
                    "broadband_plan_card"
                )
            )
            .filter(
                has=self.page.get_by_text(
                    self.data["planname"],
                    exact=True
                )
            )
        )

        selected_plan_card.get_by_role(
            "button",
            name="Choose Plan"
        ).click()

    def select_simo(self):

        selected_plan = (self.page.locator(get_locator("plans_page", "simo_plan_card")).filter(
            has=self.page.get_by_text(self.data["planname"], exact=True))
        )
        selected_plan.wait_for(state="visible")

        selected_plan.get_by_role("button", name="Choose Plan").click()

    def select_handset(self):

        device = (self.page.locator(get_locator("plans_page", "device_card")).filter(
            has=self.page.get_by_text(self.data["device_name"], exact=True))
        )
        device.wait_for(state="visible")

        device.first.click()
