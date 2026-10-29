from playwright.sync_api import Page, expect

from pageobject.base_page import BasePage


class PlansPage(BasePage):
    PAGE = "plans_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def select_plan(self):

        product = self.data["product"].lower()

        actions = {
            "broadband": self.select_broadband,
            "simo": self.select_simo,
            "handset": self.select_handset,
            "fwa": self.fwa_select_plan,
        }

        actions[product]()

    def select_broadband(self):

        if self.data["planpicker"] == "prebuilt":
            self.click_and_capture("choose_a_plan", "choose_a_plan", wait=False)

            selected_plan_card = self.locator("prebuilt_plan_card").filter(
                has=self.page.get_by_text(self.data["planname"], exact=True)
            )

            selected_plan_card.get_by_role("button", name="Choose Plan").click()

            # self.wait()

            self.capture("prebuilt_plan_selected")

            return

        selected_speed_card = self.locator("speed_card").filter(
            has_text=self.data["speed"]
        )

        selected_speed_card.get_by_role("button", name="Select").click()

        self.capture("speed_selected")

        selected_plan_card = self.locator("broadband_plan_card").filter(
            has=self.page.get_by_text(self.data["planname"], exact=True)
        )

        selected_plan_card.get_by_role("button", name="Choose Plan").click()

        expect(
            self.page.get_by_role("button", name="Continue with this plan")
        ).to_be_visible(timeout=15000)

        if self.data.get("TV_plan") != "Default":

            selected_tv_plan_card = self.locator("TV_plan_card").filter(
                has=self.page.get_by_text(self.data["TV_plan"], exact=True)
            )

            selected_tv_plan_card.get_by_role(
                "button", name="Choose TV package"
            ).click()
            expect(
                self.page.get_by_role("button", name="Continue with this TV package")
            ).to_be_enabled(timeout=15000)

        if self.data.get("plan") == "HBB":

            self.page.get_by_role("button", name="Continue to add-ons").click()

        else:
            self.page.get_by_role("button", name="Continue to setup").click()

        self.capture("broadband_plan_selected")

    def fwa_select_plan(self):

        self.page.get_by_label("5G speed", exact=True).click()

        selected_speed_card = self.locator("speed_card").filter(
            has=self.page.get_by_text(self.data["speed"], exact=True)
        )

        selected_speed_card.get_by_role("button", name="Select").click()

        self.capture("speed_selected")

        selected_plan_card = (
            self.locator("broadband_plan_card")
            .filter(has=self.page.get_by_text(self.data["planname"], exact=True))
            .filter(has=self.page.get_by_text(self.data["tenure"], exact=True))
        )

        selected_plan_card.get_by_role("button", name="Choose Plan").click()

        self.wait()

        if self.data.get("TV_plan") != "Default":

            selected_tv_plan_card = self.locator("fwa_tv_plan_card").filter(
                has=self.page.get_by_text(self.data["TV_plan"], exact=True)
            )

            selected_tv_plan_card.get_by_role("button", name="Add to plan").click()

        else:
            self.page.get_by_role("button", name="Continue to basket").click()

        self.capture("fwa_plan_selected")

    def select_simo(self):

        selected_plan = (
            self.locator("simo_plan_card")
            .filter(has=self.page.get_by_text(self.data["planname"], exact=True))
            .first
        )

        selected_plan.wait_for(state="visible")

        selected_plan.get_by_role("button", name="Choose Plan").click()

        self.wait()

        if self.data.get("TV_plan") != "Default":

            selected_tv_plan_card = self.locator("simo_tv_plan_card").filter(
                has=self.page.get_by_text(self.data["TV_plan"], exact=True)
            )

            selected_tv_plan_card.get_by_role("button", name="Add to plan").click()

        else:
            self.page.get_by_role(
                "button", name="Continue without entertainment"
            ).click()

        self.capture("simo_plan_selected")

    def select_handset(self):

        device = self.locator("device_card").filter(
            has=self.page.get_by_text(self.data["device_name"], exact=True)
        )

        self.scroll_until_visible(device)

        device.click()

        self.capture("device_selected")
