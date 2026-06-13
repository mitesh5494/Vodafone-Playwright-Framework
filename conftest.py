import os

import pytest
from playwright.sync_api import sync_playwright

from utils.screenshot_manager import ScreenshotManager


def pytest_addoption(parser):
    parser.addoption(
        "--browsername",
        action="store",
        default="chrom"
    )

    parser.addoption(
        "--url",
        action="store",
        default="https://www.vodafone.co.uk/broadband"
    )


@pytest.fixture(scope="session")
def browser_instance(request):
    browser_name = request.config.getoption("--browsername")

    playwright = sync_playwright().start()

    is_ci = os.getenv("CI") == "true"

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
    urlname = request.config.getoption("--url")

    context = browser_instance.new_context()

    page = context.new_page()

    page.goto(urlname)

    yield page

    context.close()


@pytest.fixture
def report():
    """
    Screenshot manager fixture.
    Creates Word report automatically after test execution.
    """
    manager = ScreenshotManager()

    yield manager

    if manager.test_case_name and manager.screenshot_paths:
        manager.create_word_report()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically capture failure screenshot
    and add it to Word report.
    """

    outcome = yield
    report_result = outcome.get_result()

    if (
            report_result.when == "call"
            and report_result.failed
    ):

        page = item.funcargs.get("page")
        report = item.funcargs.get("report")

        if page and report:
            report.capture_failure(
                page,
                str(report_result.longrepr)
            )
