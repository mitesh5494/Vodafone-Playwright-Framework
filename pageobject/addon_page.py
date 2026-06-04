
class AddonPage:
    def __init__(self, page):
        self.page = page


    def continue_to_setup_page(self):
        self.page.get_by_role("button", name="Continue").click()