from utils.locator_loader import get_locator


class AirtimePlansPage:

    def __init__(self, page, data):
        self.page = page
        self.data = data

    def select_airtime_plan(self):

        plan = (
            self.page
            .locator(
                get_locator(
                    "airtime_page",
                    "airtime_plan"
                )
            )
            .filter(
                has_text=self.data["planname"]
            )
        )

        plan.click()

        self.page.locator(
            get_locator(
                "airtime_page",
                "continue_btn"
            )
        ).click()