import pytest

from wargaming_test import storages


@pytest.mark.parametrize(
    'start, end, collection',
    [
        (0, 5, [1, 1, 2, 3, 5]),
        (1, 5, [1, 2, 3, 5]),
    ],
)
async def test_get_fibonacci(start, end, collection):
    assert list(storages.fibonacci_slice.get(start, end)) == collection


async def test_get_fibonacci_cached(fibonacci_slice):
    # Здесь не используется @pytest.mark.parametrize
    # поскольку сравниваются состояния fibonacci_slice
    # между вызовами
    fibonacci_slice.get(0, 3)
    assert fibonacci_slice.refresh_collection_count == 0

    fibonacci_slice.get(0, 10)
    assert fibonacci_slice.refresh_collection_count == 0

    fibonacci_slice.get(0, 11)
    assert fibonacci_slice.refresh_collection_count == 1

    fibonacci_slice.get(0, 12)
    assert fibonacci_slice.refresh_collection_count == 2

    fibonacci_slice.get(0, 11)
    assert fibonacci_slice.refresh_collection_count == 2
