import pytest


@pytest.fixture
def array():
    yield [1, 2, 3]