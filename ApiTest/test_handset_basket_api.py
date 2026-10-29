import re

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect, sync_playwright


PAY_MONTHLY_URL = (
    "https://www.vodafone.co.uk/mobile/pay-monthly-contracts"
    "?icmp=CBU_Home_QLBanner_P1_PAYM_26/03/2026"
)
HANDSET_NAME = "Iphone 17"


@pytest.mark.parametrize("handset_name", [HANDSET_NAME])
def test_handset_basket_api_response(handset_name):
    handset_slug = re.sub(r"[^a-z0-9]+", "-", handset_name.casefold()).strip("-")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            page = browser.new_page()
            page.goto(PAY_MONTHLY_URL, wait_until="domcontentloaded")

            accept_cookies = page.locator("#onetrust-accept-btn-handler")
            try:
                accept_cookies.wait_for(state="visible", timeout=5000)
            except PlaywrightTimeoutError:
                pass
            else:
                accept_cookies.click()

            page.goto(
                f"https://www.vodafone.co.uk/mobile/pay-monthly-contracts/apple/{handset_slug}",
                wait_until="domcontentloaded",
            )
            expect(page).to_have_url(
                re.compile(rf"/apple/{re.escape(handset_slug)}(?:#|$)"),
                timeout=30000,
            )

            page.get_by_role("button", name="I'm a new customer").click()
            page.get_by_role("button", name="Build your own plan").click()

            continue_without_trade_in = page.get_by_role(
                "button", name="Continue without trade in"
            )
            phone_plan_heading = page.get_by_role(
                "heading", name="Build your Phone Plan"
            )

            try:
                continue_without_trade_in.wait_for(
                    state="visible", timeout=8000
                )
            except PlaywrightTimeoutError:
                pass
            else:
                continue_without_trade_in.click()

            if not phone_plan_heading.is_visible():
                choose_plans = page.get_by_role(
                    "button", name="Choose these plans", exact=True
                )
                expect(choose_plans.first).to_be_visible(timeout=30000)
                choose_plans.first.click()

                expect(continue_without_trade_in).to_be_visible(timeout=15000)
                continue_without_trade_in.click()

            expect(phone_plan_heading).to_be_visible(timeout=30000)
            page.get_by_role("button", name="Continue", exact=True).click()

            airtime_cards = page.locator(
                '[data-selector="new-airtime-plans-cards-single-column-card"]'
            )
            expect(airtime_cards.first).to_be_visible(timeout=30000)
            airtime_card = airtime_cards.first
            airtime_plan_name = airtime_card.locator("h2").first.inner_text().strip()
            airtime_card.get_by_role(
                "button", name="Choose plan", exact=True
            ).click()

            continue_without_entertainment = page.locator(
                'button[aria-label="Continue without entertainment"]'
            )
            expect(continue_without_entertainment).to_be_enabled(timeout=30000)
            continue_without_entertainment.click()

            expect(page).to_have_url(re.compile(r"#add-ons$"), timeout=30000)

            with page.expect_response(
                lambda response: (
                    "/basket/api/basket/v2/basket/" in response.url
                    and response.request.method == "GET"
                ),
                timeout=30000,
            ) as basket_response_info:
                page.get_by_role("button", name="Continue", exact=True).click()

            basket_response = basket_response_info.value
            assert basket_response.status == 200, (
                f"Basket API returned HTTP {basket_response.status}"
            )
            basket = basket_response.json()

            handset_package = next(
                (
                    package
                    for package in basket.get("packages", [])
                    if package.get("bundle", {}).get("bundleClass") == "HANDSET"
                ),
                None,
            )
            assert handset_package is not None, "No handset package in basket API response"
            assert any(
                hardware.get("model") == handset_slug
                for hardware in handset_package.get("hardwares", [])
            ), f"{handset_name} not found in basket API response"
            assert (
                handset_package.get("bundle", {}).get("displayName")
                == airtime_plan_name
            ), (
                "Selected airtime plan does not match the basket API response: "
                f"expected {airtime_plan_name!r}, got "
                f"{handset_package.get('bundle', {}).get('displayName')!r}"
            )

            expect(page).to_have_url(re.compile(r"/basket(?:\?.*)?$"), timeout=30000)
            expect(
                page.get_by_role("heading", name="Review your basket")
            ).to_be_visible()
        finally:
            browser.close()
