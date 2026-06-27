from playwright.sync_api import Page, Playwright
from pytest_html.report import Report


def hbb_api(playwright: Playwright):
    playwright.request.new_context()