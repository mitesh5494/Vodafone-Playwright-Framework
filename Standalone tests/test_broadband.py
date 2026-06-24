import json
import time

from playwright.sync_api import Page

from utils.test_data_loader import get_test_data


def test_new_acq_order(page: Page):
    # Json reader
    data = get_test_data("FTTP_TC_Acq")

    # landing page
    page.goto("https://www.vodafone.co.uk/broadband")
    page.get_by_role("button", name="Accept all cookies").click()
    page.get_by_placeholder("e.g. SE1 0BE").fill(data["postcode"])
    page.get_by_role("button", name="Check availability").click()
    # Address page
    page.locator("#address").select_option(data["housenum"])
    page.locator("label[for='lineOption-1']").click()
    page.locator("label[for='journeyOption-1']").click()
    page.locator("button[aria-label='false']").click()
    # plans page
    if data["planpicker"] == "prebuilt":
        page.locator("input[value='preBuilt']").check()  # (Choose a plan)

    else:
        page.locator("div[class='sc-kUuIQH euVcxp']").filter(has_text=data["speed"]).get_by_role("button",
                                                                                                 name="Select").click()
    if data["plantype"] == "extra":
        page.locator("span[data-title='Broadband + TV']").click()

    card = page.locator("div[class='sc-fWMeal jvrYwf']").filter(has=page.get_by_text(data["planname"], exact=True))
    card.get_by_role("button", name="Choose Plan").click()

    # Add on page
    page.get_by_role("button", name="Continue").click()

    # Broadband Setup page
    print(page.locator("div[class='sc-dMmcxd ZrFkH'] div[class='sc-dFVmKS haRLPe']").nth(0).text_content())
    page.locator("#read-and-agreed").check()
    page.locator("#select").select_option(index=1)
    page.locator("label[id='digital-voice-checkbox-digitalVoice'] p[class='sc-iIvHqT czvOrG']").check()
    page.locator("label[id='digital-voice-checkbox-telecare'] p[class='sc-iIvHqT czvOrG']").check()
    page.get_by_role("button", name="Go to basket").click()



    time.sleep(2)
