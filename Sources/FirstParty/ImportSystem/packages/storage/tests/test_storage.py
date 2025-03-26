import pytest

from storage.storage import Storage


def test_storage_1():
    s = Storage()
    assert not s.has_value()
