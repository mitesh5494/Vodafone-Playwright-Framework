from playwright.sync_api import Page, expect

from utils.test_data_loader import get_test_data
from utils.locator_loader import get_locator


class BasketPage:

    def __init__(self, page: Page, data):
        self.page = page
        self.data = data

    def expand_buttons(self):
        self.page.get_by_role("button").filter(has=self.page.get_by_text(self.data["planname"])).click()

        add_on = self.page.get_by_role("button").filter(has=self.page.get_by_text("Add Ons"))
        if add_on.count() > 0:
            add_on.click()
        self.page.get_by_role("button").filter(has=self.page.get_by_text("Promotional code")).click()
        discount=self.page.get_by_role("button").filter(has=self.page.get_by_text("Your discount overview"))
        if discount.count() > 0:
            discount.click()
        self.page.get_by_role("button").filter(has=self.page.get_by_text("VAT breakdown")).click()

    def plan_validation(self):
        expect(self.page.locator("h4").filter(has=self.page.get_by_text(self.data["planname"])))
        hardwares = (self.page.locator("ul [data-component-name='ListGroup']").all_text_contents())
        # print(hardwares)

    def image_validation(self):
        expected = [
            "Ultra Hub with WiFi 7",
            "Super WiFi 7",
            "4G Broadband Back-up"
        ]

        actual = self.page.locator(
            "div[data-selector='package-body'] picture img[alt]"
        ).evaluate_all(
            "(els) => [...new Set(els.map(e => e.alt))]"
        )

        assert actual == expected

    def hardware_validation(self):
        equipments = self.page.locator(get_locator("basket_page", "equipments_list")).all_text_contents()

        cleaned = list(dict.fromkeys([text.strip() for text in equipments if text.strip()]))

        print(cleaned)

    def go_to_checkout(self):
        self.page.get_by_role("button").filter(has=self.page.get_by_text("Go to checkout")).last.click()
