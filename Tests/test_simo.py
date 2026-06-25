import time

from playwright.sync_api import Page

from pageobject.basket_page import BasketPage
from pageobject.checkout_page import CheckoutPage
from pageobject.landing_page import LandingPage
from pageobject.plans_page import PlansPage
from utils.test_data_loader import get_test_data


def test_simo_tc_acq(page: Page, report):
    # json reader and report
    test_case_name = "simo_tc_acq"
    report.start_test(test_case_name)
    data = get_test_data(test_case_name)

    # landing page
    landing = LandingPage(page)
    landing.accept_cookies()

    # plans page
    plan = PlansPage(page, data)
    plan.select_plan()

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
