"""Shopping cart tests. All stable except test_checkout, which mimics a real
race condition: the checkout button occasionally isn't clickable yet when the
test looks for it."""
import random


def test_add_item():
    cart = []
    cart.append("widget")
    assert cart == ["widget"]


def test_remove_item():
    cart = ["widget", "gadget"]
    cart.remove("widget")
    assert cart == ["gadget"]


def test_apply_coupon():
    price, discount = 100, 0.1
    assert round(price * (1 - discount)) == 90


def test_checkout():
    # ~6% of the time, the checkout button isn't clickable within the timeout yet.
    if random.random() < 0.06:
        raise AssertionError("Timeout waiting for #checkout-button to become clickable")
    assert True