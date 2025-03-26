import pytest

from network.network import Network


def test_network_1():
    n = Network()
    assert n.has_value()
