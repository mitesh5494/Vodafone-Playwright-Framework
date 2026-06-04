from utils.locator_loader import get_locator


class BBSetupPage:
    def __init__(self, page):
        self.page = page

    def continue_to_basket_page(self):

        print(self.page.locator(get_locator("setup_page","line_info")).nth(0).text_content())
        self.page.locator(get_locator("setup_page","bill_payer_checkbox")).check()
        self.page.locator(get_locator("setup_page","date_dropdown")).select_option(index=1)
        self.page.locator(get_locator("setup_page","digital_voice_checkbox")).check()
        self.page.locator(get_locator("setup_page","telecare_checkbox")).check()
        self.page.get_by_role("button", name="Go to basket").click()