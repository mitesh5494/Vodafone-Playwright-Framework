import json
import urllib

from playwright.sync_api import Playwright


def test_get_session(playwright: Playwright):

    response = playwright.request.new_context().get('https://www.vodafone.co.uk/web-shop/login/auth/session')
    print(response.status)
    headers=response.headers_array
    get_cookie_value(headers, 'set-cookie')





    #print(response.json())



def get_cookie_value(headers, key):
    # Collect all Set-Cookie values (case-insensitive)
    cookies = [h['value'] for h in headers if h['name'].lower() == 'set-cookie']

    # Loop through cookies to find the JSON-based one
    json_cookie = None
    for cookie in cookies:
        decoded = urllib.parse.unquote(cookie)
        if decoded.startswith("j:"):  # JSON-based cookie
            json_str = decoded[2:].split(';')[0]  # remove "j:" and trailing attributes
            try:
                json_cookie = json.loads(json_str)
                break  # stop once we successfully parse
            except json.JSONDecodeError:
                continue


    # Print the platformSessionId if found
    if json_cookie:

      print("platformSessionId:", json_cookie.get("platformSessionId"))




