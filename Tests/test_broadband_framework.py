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
    test_case_name = "fttp_tc_acq"

    report.start_test(test_case_name)

    data = get_test_data(test_case_name)

    landing = LandingPage(page, data, report)

    landing.accept_cookies()
    landing.check_availability()

    address = AddressPage(page, data, report)

    address.bbl_view_broadband_plans()

    plan = PlansPage(page, data, report)

    plan.select_plan()

    addon = AddonPage(page, data, report)

    addon.select_hbb_addon()
    addon.continue_to_setup_page()

    setup = BBSetupPage(page, report)

    setup.continue_to_basket_page()

    basket = BasketPage(page, data, report)

    basket.basket_expand_arrows()
    basket.basket_validation()
    basket.go_to_checkout()

    checkout = CheckoutPage(page, data, report)

    checkout.checkout()


def test_ftth_tc_acq(page: Page, report):
    test_case_name = "ftth_tc_acq"

    report.start_test(test_case_name)

    data = get_test_data(test_case_name)

    landing = LandingPage(page, data, report)

    landing.accept_cookies()
    landing.check_availability()

    address = AddressPage(page, data, report)

    address.bbl_view_broadband_plans()

    plan = PlansPage(page, data, report)

    plan.select_plan()

    addon = AddonPage(page, data, report)

    addon.plan_validation()
    addon.continue_to_setup_page()

    setup = BBSetupPage(page, report)

    setup.continue_to_basket_page()

    basket = BasketPage(page, data, report)

    basket.basket_expand_arrows()
    basket.basket_validation()
    basket.go_to_checkout()

    checkout = CheckoutPage(page, data, report)

    checkout.checkout()


def test_sogea_tc_acq(page: Page, report):
    test_case_name = "sogea_tc_acq"

    report.start_test(test_case_name)

    data = get_test_data(test_case_name)

    landing = LandingPage(page, data, report)

    landing.accept_cookies()
    landing.check_availability()

    address = AddressPage(page, data, report)

    address.bbl_view_broadband_plans()

    plan = PlansPage(page, data, report)

    plan.select_plan()

    addon = AddonPage(page, data, report)

    addon.plan_validation()
    addon.continue_to_setup_page()

    setup = BBSetupPage(page, report)

    setup.continue_to_basket_page()

    basket = BasketPage(page, data, report)

    basket.basket_expand_arrows()
    basket.basket_validation()
    basket.go_to_checkout()

    checkout = CheckoutPage(page, data, report)

    checkout.checkout()
