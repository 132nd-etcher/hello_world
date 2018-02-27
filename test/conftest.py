# coding=utf-8

import sys
from pathlib import Path
import os
import pytest


def pytest_configure(config):
    """
    Runs at tests startup

    Args:
        config: pytest config args
    """
    print('Pytest config:', config.option)
    setattr(sys, '_called_from_test', True)


# noinspection SpellCheckingInspection
def pytest_unconfigure(config):
    """Tear down"""
    assert config
    delattr(sys, '_called_from_test')


def pytest_addoption(parser):
    parser.addoption("--long", action="store_true",
                     help="run long tests")


def pytest_runtest_setup(item):
    long_marker = item.get_marker("long")
    if long_marker is not None and not item.config.getoption('long'):
        pytest.skip('skipping long tests')


# @pytest.fixture(autouse=True)
# def _dummy():
#     path = sys.path
#     here = Path('.').parent.absolute()
#     sys.path.append(str(here))
#     print(sys.path)
#     yield
#     sys.path.remove(here)
#     sys.path = path
