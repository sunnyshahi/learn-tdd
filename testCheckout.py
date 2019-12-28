import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTOtalWithMultipleItems(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3