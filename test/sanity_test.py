import pytest_collector


def test_sanity():
    for module in pytest_collector.collect("./example_suites"):
        print(module)
