import time

from playwright.sync_api import Page

from pageobject.addon_page import AddonPage
from pageobject.airtime_plans_page import AirtimePlansPage
from pageobject.basket_page import BasketPage
from pageobject.checkout_page import CheckoutPage
from pageobject.device_variants_page import DeviceVariantsPage
from pageobject.landing_page import LandingPage
from pageobject.phoneplan_page import PhonePlanPage
from pageobject.plans_page import PlansPage
from utils.test_data_loader import get_test_data


def test_handsetpaym_tc_acq(page:Page, report):
    # json reader and report
    test_case_name = "handsetpaym_tc_acq"
    report.start_test(test_case_name)
    data = get_test_data(test_case_name)

    # landing page
    landing = LandingPage(page)
    landing.accept_cookies()
    report.capture(page, "Landing Page")



    # plans page
    plan = PlansPage(page, data)
    plan.select_plan()
    report.capture(page, "Plan Details")

    # DeviceVariantsPage
    devicevarient = DeviceVariantsPage(page, data)
    devicevarient.configure_device()
    report.capture(page, "Device Variant Details")

    # phoneplan page
    phoneplan=  PhonePlanPage(page, data)
    phoneplan.select_contract()
    report.capture(page, "Phone Plan tenure")

    # AirtimePlansPage
    airtimeplan=AirtimePlansPage(page, data)
    airtimeplan.select_airtime_plan()
    report.capture(page, "Airtime Plan Details")

    #Add on page
    addon= AddonPage(page, data)
    addon.select_handset_addon()

    # Basket page
    basket = BasketPage(page, data)
    basket.basket_expand_arrows()
    report.capture(page, "Basket Page")


    time.sleep(2)