import os

import pytest
from playwright.sync_api import sync_playwright

from utils.screenshot_manager import ScreenshotManager
from utils.test_data_loader import get_test_data


PRODUCT_URLS = {

    "broadband":
        "https://www.vodafone.co.uk/broadband?icmp=CBU_Home_QLBanner_P3_HBB_26/03/2026",

    "simo":
        "https://www.vodafone.co.uk/sim-only/best-sim-only-deals?icmp=CBU_Home_QLBanner_P2_SIMO_26/03/2026",

    "handset":
        "https://www.vodafone.co.uk/mobile/pay-monthly-contracts?icmp=CBU_Home_QLBanner_P1_PAYM_26/03/2026"
}


def pytest_addoption(parser):

    parser.addoption(
        "--browsername",
        action="store",
        default="chrom"
    )


@pytest.fixture(scope="session")
def browser_instance(request):

    browser_name = request.config.getoption(
        "--browsername"
    )

    playwright = sync_playwright().start()

    is_ci = os.getenv(
        "CI"
    ) == "true"

    headless = True if is_ci else False

    if browser_name == "chrom":

        browser = playwright.chromium.launch(
            headless=headless
        )

    elif browser_name == "firefox":

        browser = playwright.firefox.launch(
            headless=headless
        )

    else:

        browser = playwright.chromium.launch(
            headless=headless
        )

    yield browser

    browser.close()

    playwright.stop()


@pytest.fixture
def page(browser_instance, request):

    test_function = request.node.name

    test_case = test_function.replace(
        "test_",
        ""
    )

    data = get_test_data(
        test_case
    )

    product = data[
        "product"
    ].lower()

    url = PRODUCT_URLS.get(
        product
    )

    if not url:

        raise Exception(
            f"URL not configured for product: {product}"
        )

    context = browser_instance.new_context()

    page = context.new_page()

    page.goto(
        url
    )

    yield page

    context.close()


@pytest.fixture
def report():
    """
    Screenshot manager fixture.
    Creates Word report automatically.
    """

    manager = ScreenshotManager()

    yield manager

    if (
        manager.test_case_name
        and manager.screenshot_paths
    ):

        manager.create_word_report()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
        item,
        call
):
    """
    Capture failure screenshot
    and attach to Word report
    """

    outcome = yield

    report_result = outcome.get_result()

    if (
        report_result.when == "call"
        and report_result.failed
    ):

        page = item.funcargs.get(
            "page"
        )

        report = item.funcargs.get(
            "report"
        )

        if page and report:

            report.capture_failure(
                page,
                str(
                    report_result.longrepr
                )
            )