import json
import urllib
from http.client import responses

from playwright.sync_api import Playwright


def test_verify_login(playwright: Playwright):
    # Create API request context
    request_context = playwright.request.new_context()

    # Send POST request
    response = request_context.post("https://automationexercise.com/api/verifyLogin", form={"email": "test@test.com", "password": "123456"})

    # Validate HTTP status
    assert response.status == 200

    # Convert response to JSON
    response_body = response.json()

    print(response_body)



