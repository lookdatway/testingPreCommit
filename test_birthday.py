from birthday import *  # The code to test
import pytest


@pytest.fixture
def exampleBirthday():
    data = {"yyyy": 2002, "mm": 11, "dd": 23}
    return data


def test_birthday(exampleBirthday):
    assert (
        get_age(exampleBirthday["yyyy"], exampleBirthday["mm"], exampleBirthday["dd"])
        > 20
        and get_age(
            exampleBirthday["yyyy"], exampleBirthday["mm"], exampleBirthday["dd"]
        )
        < 21
    )


def test_sums(exampleBirthday):
    assert (
        sum(exampleBirthday["yyyy"], exampleBirthday["mm"], exampleBirthday["dd"])
        == 2036
    )
