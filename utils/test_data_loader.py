import json
from pathlib import Path


def get_test_data(test_case_name):
    file_path = Path(__file__).parent.parent / "test_data" / "testdata.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return data[test_case_name]
