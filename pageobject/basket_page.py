from playwright.sync_api import Page, expect

from pageobject.base_page import BasePage


class BasketPage(BasePage):
    PAGE = "basket_page"

    def __init__(self, page: Page, data, report=None):

        super().__init__(page, report)

        self.data = data

    def basket_expand_arrows(self):

        expand_btn = self.locator("expand")

        expect(expand_btn.first).to_be_visible(timeout=10000)

        while True:

            count = expand_btn.count()

            if count == 0:
                break

            expand_btn.last.click(force=True)

            self.page.wait_for_timeout(1000)

            if expand_btn.count() == count:
                break

        self.capture("basket_expanded")

    def basket_validation(self):

        if self.data["product"] == "broadband":

            self.__plan_validation()

            self.__hardware_validation()

        elif self.data["product"] in ["simo", "handset"]:

            self.__plan_validation()

        self.capture("basket_validated")

    def __plan_validation(self):

        plan = (self.page.locator("h4").filter(has=self.page.get_by_text(self.data["planname"])))

        expect(plan).to_be_visible()

    def __hardware_validation(self):

        equipments = (self.locator("equipments_list").all_text_contents())

        cleaned = list(dict.fromkeys([text.strip() for text in equipments if text.strip()]))

        print(cleaned)

    def go_to_checkout(self):

        (self.page.get_by_role("button").filter(has=self.page.get_by_text("Go to checkout")).last.click())

        self.wait()

        self.capture("go_to_checkout")
