"""Simple collecting test."""

import pytest_collector


def test_sanity() -> None:
    """
    Collect the example suites.

    :return: Nothing
    """
    for module in pytest_collector.collect("./example_suites"):
        print(module)
