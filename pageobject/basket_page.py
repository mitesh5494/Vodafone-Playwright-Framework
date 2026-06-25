from playwright.sync_api import Page, expect

from utils.test_data_loader import get_test_data
from utils.locator_loader import get_locator


class BasketPage:

    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def basket_expand_arrows(self):
        selector = "#basket-fed-module-styles-container .sc-tOkKi.jMzKTg svg"

        self.page.wait_for_selector(selector)

        while True:

            arrows = self.page.locator(selector)

            count = arrows.count()

            if count == 0:
                break

            arrows.last.click(force=True)

            self.page.wait_for_timeout(1000)

    def basket_validation(self):
        if self.data["product"] == "broadband":
            self.__plan_validation()
            self.__hardware_validation()


        elif self.data["product"] == "simo":
            self.__plan_validation()

        elif self.data["product"] == "handset":
            self.__plan_validation()

    def __plan_validation(self):
        expect(self.page.locator("h4").filter(has=self.page.get_by_text(self.data["planname"])))
        hardwares = (self.page.locator("ul [data-component-name='ListGroup']").all_text_contents())
        # print(hardwares)

    def __hardware_validation(self):
        equipments = self.page.locator(get_locator("basket_page", "equipments_list")).all_text_contents()

        cleaned = list(dict.fromkeys([text.strip() for text in equipments if text.strip()]))

        print(cleaned)

    def go_to_checkout(self):
        self.page.get_by_role("button").filter(has=self.page.get_by_text("Go to checkout")).last.click()
