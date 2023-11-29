import json
import os
from library import Library
import pytest

@pytest.fixture
def create_test_json_file():
    data = {
        "books": ["harry potter 1", "harry potter 2"],
        "customers": []
    }
    with open("data.json", "w") as f:
        json.dump(data, f)

    yield data # Everything after this, will happen at the end of test
    os.unlink("data.json")


def test_empty_library():
    new_library = Library("test.json")
    assert new_library.data == {}


def test_good_library(create_test_json_file):
    new_library = Library("data.json")
    assert new_library.data == create_test_json_file
