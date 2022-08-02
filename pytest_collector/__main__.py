import sys

import pytest_collector


def main():
    pytest_collector.collect(sys.argv[0])


if __name__ == '__main__':
    main()
