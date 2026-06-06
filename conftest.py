import pytest
from playwright.sync_api import sync_playwright


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

    if browser_name == "chrom":
        browser = playwright.chromium.launch(headless=False)

    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

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

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"reports/{item.name}.png")
