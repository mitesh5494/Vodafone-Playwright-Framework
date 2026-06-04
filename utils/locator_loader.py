import json
from pathlib import Path


def get_locator(page_name, locator_name):
    file_path = Path(__file__).parent.parent / "test_data" / "locators.json"

    with open(file_path) as f:
        data = json.load(f)

    return data[page_name][locator_name]