import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_CanAddItemPrice(checkout):
    co.addItemPrice("a", 1)

def test_canAddItem(checkout):
    co.addItem("a")