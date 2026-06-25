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
    # JSON reader and report
    test_case_name = "fttp_tc_acq"
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
    plan.select_plan()
    report.capture(page, "Plans Page")

    # Add on page
    addon = AddonPage(page, data)
    addon.select_hbb_addon()

    report.capture(page, "Addons Page")
    addon.continue_to_setup_page()

    # Broadband Setup page
    setup = BBSetupPage(page)

    setup.continue_to_basket_page()
    report.capture(page, "Setup Page")

    # Basket page
    basket = BasketPage(page, data)
    basket.basket_expand_arrows()
    report.capture(page, "Basket Page")
    basket.basket_validation()
    basket.go_to_checkout()

    # Checkout page
    checkout = CheckoutPage(page, data)
    checkout.checkout()
    report.capture(page, "Checkout Page")

    time.sleep(2)


def test_ftth_tc_acq(page: Page, report):
    # Json reader
    test_case_name = "ftth_tc_acq"
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
    plan.select_plan()
    report.capture(page, "Plans Page")

    # Add on page
    addon = AddonPage(page, data)
    # addon.select_addon()
    addon.__plan_validation()
    report.capture(page, "Addons Page")
    addon.continue_to_setup_page()

    # Broadband Setup page
    setup = BBSetupPage(page)

    setup.continue_to_basket_page()
    report.capture(page, "Setup Page")

    # Basket page
    basket = BasketPage(page, data)
    basket.basket_expand_arrows()
    report.capture(page, "Basket Page")
    basket.__basket_validation()
    basket.go_to_checkout()

    # Checkout page
    checkout = CheckoutPage(page, data)
    checkout.checkout()
    report.capture(page, "Checkout Page")

    time.sleep(2)


def test_sogea_tc_acq(page: Page, report):
    # Json reader
    test_case_name = "sogea_tc_acq"
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
    plan.select_plan()
    report.capture(page, "Plans Page")

    # Add on page
    addon = AddonPage(page, data)
    # addon.select_addon()
    addon.__plan_validation()
    report.capture(page, "Addons Page")
    addon.continue_to_setup_page()

    # Broadband Setup page
    setup = BBSetupPage(page)

    setup.continue_to_basket_page()
    report.capture(page, "Setup Page")

    # Basket page
    basket = BasketPage(page, data)
    basket.basket_expand_arrows()
    report.capture(page, "Basket Page")
    basket.__basket_validation()
    basket.go_to_checkout()

    # Checkout page
    checkout = CheckoutPage(page, data)
    checkout.checkout()
    report.capture(page, "Checkout Page")

    time.sleep(2)
