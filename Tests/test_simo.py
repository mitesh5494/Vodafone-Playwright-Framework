import time

from playwright.sync_api import Page

from pageobject.basket_page import BasketPage
from pageobject.checkout_page import CheckoutPage
from pageobject.landing_page import LandingPage
from pageobject.plans_page import PlansPage
from utils.test_data_loader import get_test_data


def test_simo_tc_acq(page:Page, report):
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
    basket.expand_buttons()
    report.capture(page, "Basket Page")
    basket.plan_validation()
    basket.hardware_validation()
    basket.go_to_checkout()

    # Checkout page
    checkout = CheckoutPage(page, data)
    checkout.fill_about_you()
    report.capture(page, "Checkout Page Customer Details")
    checkout.address_detail()
    checkout.continue_to_broadband()
    report.capture(page, "Checkout Page Address Details")
    checkout.choose_your_delivery_address_and_continue_to_payment()
    report.capture(page, "Checkout Page Delivery Details")
    checkout.bank_acc_details_and_continue()
    report.capture(page, "Checkout Page Bank Details")

    time.sleep(2)