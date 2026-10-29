import re

import pytest
from playwright.sync_api import expect, sync_playwright

PRODUCT_ASIN = "B0GX9CBCBV"
PRODUCT_TITLE = (
    "vivo X300 FE 5G (Noir Black, 12GB RAM, 512GB Storage) "
    "with No Cost EMI/Additional Exchange Offers"
)
PRODUCT_URL = f"https://www.amazon.in/dp/{PRODUCT_ASIN}"


@pytest.mark.parametrize(
    ("asin", "product_title"),
    [(PRODUCT_ASIN, PRODUCT_TITLE)],
)
def test_amazon_cart_api_contains_selected_product(asin, product_title):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            page = browser.new_page()
            page.goto(PRODUCT_URL, wait_until="domcontentloaded")

            expect(page.locator("#ASIN")).to_have_value(asin)
            expect(page).to_have_title(re.compile(re.escape(product_title)))

            with page.expect_response(
                lambda response: (
                    "/cart/add-to-cart/get-cart-items" in response.url
                    and response.request.method == "GET"
                ),
                timeout=30000,
            ) as cart_api_response_info:
                page.locator("#add-to-cart-button").click()

            cart_api_response = cart_api_response_info.value
            assert cart_api_response.status == 200, (
                "Amazon cart API returned " f"HTTP {cart_api_response.status}"
            )

            cart_items = cart_api_response.json()
            assert isinstance(
                cart_items, list
            ), "Amazon cart API response should be a list of cart items"
            assert any(
                item.get("asin") == asin and item.get("quantity") == 1
                for item in cart_items
            ), f"Expected ASIN {asin} with quantity 1 in cart API response"

            expect(page.get_by_text("Added to cart", exact=True)).to_be_visible(
                timeout=15000
            )
        finally:
            browser.close()
