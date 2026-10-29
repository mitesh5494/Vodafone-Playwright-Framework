import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect, sync_playwright


SIMO_URL = (
    "https://www.vodafone.co.uk/sim-only/best-sim-only-deals"
    "?icmp=CBU_Home_QLBanner_P2_SIMO_26/03/2026"
)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            page = browser.new_page()
            page.goto(SIMO_URL, wait_until="domcontentloaded")

            accept_cookies = page.locator("#onetrust-accept-btn-handler")
            try:
                accept_cookies.wait_for(state="visible", timeout=5000)
            except PlaywrightTimeoutError:
                pass
            else:
                accept_cookies.click()

            choose_plan_name = re.compile("^choose plan$", re.IGNORECASE)
            plan_card = (
                page.locator('[data-component-name="SingleColumnCard"]')
                .filter(has=page.get_by_role("button", name=choose_plan_name))
                .first
            )
            expect(plan_card).to_be_visible(timeout=30000)
            plan_summary = " | ".join(
                line.strip()
                for line in plan_card.inner_text().splitlines()
                if line.strip()
            )
            plan_card.get_by_role("button", name=choose_plan_name).click()

            page.get_by_role(
                "button", name="Continue without entertainment"
            ).click(timeout=15000)

            expect(page).to_have_url(re.compile(r"/basket/?$"), timeout=30000)
            expect(
                page.get_by_role("heading", name="Review your basket")
            ).to_be_visible()
            print(f"Reached basket with selected SIM-only offer: {plan_summary}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
