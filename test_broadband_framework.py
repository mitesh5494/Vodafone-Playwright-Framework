import json
import time

from playwright.sync_api import Page

from pageobject.addon_page import AddonPage
from pageobject.address_page import AddressPage
from pageobject.basket_page import BasketPage
from pageobject.bbsetup_page import BBSetupPage
from pageobject.checkout_page import CheckoutPage
from pageobject.landing_page import LandingPage
from pageobject.plans_page import PlansPage

from utils.test_data_loader import get_test_data


def test_fttp_tc_acq(page: Page, report):
    # Json reader
    test_case_name = "FTTP_TC_Acq"
    report.start_test(test_case_name)
    data = get_test_data(test_case_name)

    # landing page
    landing = LandingPage(page)
    landing.accept_cookies()
    landing.enter_postcode(data["postcode"])
    report.capture(page, "Landing Page")
    landing.click_check_availability()

    # Address page
    address = AddressPage(page, data)

    address.bbl_view_broadband_plans()
    report.capture(page, "Address Page")

    # plans page
    plan = PlansPage(page, data)

    plan.build_a_plan()
    report.capture(page, "Plans Page")

    # Add on page
    addon = AddonPage(page, data)
    # addon.select_addon()
    report.capture(page, "Addons Page")
    addon.continue_to_setup_page()


    # Broadband Setup page
    setup = BBSetupPage(page)

    setup.continue_to_basket_page()
    report.capture(page, "Setup Page")

    # Basket page
    basket = BasketPage(page, data)
    basket.expand_buttons()
    report.capture(page, "Basket Page")
    basket.plan_validation()
    basket.hardware_validation()
    basket.go_to_checkout()

    #Checkout page
    checkout=CheckoutPage(page,data)
    checkout.fill_about_you()
    #report.capture(page, "Checkout Page Customer Details")
    checkout.continue_to_add_detail()
    report.capture(page, "Checkout Page Customer Details")

    time.sleep(2)
