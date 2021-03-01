import os
import sys

import pytest

from wargaming_test import storages
from wargaming_test.app import get_web_app

pytest_plugins = [
    "aiohttp.pytest_plugin",
]


my_path = os.path.dirname(os.path.abspath(__file__))  # pylint: disable=invalid-name
sys.path.insert(0, my_path + "/../")


@pytest.fixture
async def client(aiohttp_client, loop):  # pylint: disable=unused-argument
    client = await aiohttp_client(get_web_app())
    yield client


@pytest.fixture
async def fibonacci_slice(monkeypatch, loop):
    original_refresh_collection = storages.fibonacci_slice._refresh_collection

    def mocked_refresh_collection(n):
        storages.fibonacci_slice.refresh_collection_count += 1
        return original_refresh_collection(n)

    monkeypatch.setattr(storages.fibonacci_slice, '_refresh_collection', mocked_refresh_collection)

    setattr(storages.fibonacci_slice, 'refresh_collection_count', 0)

    yield storages.fibonacci_slice

    delattr(storages.fibonacci_slice, 'refresh_collection_count')
