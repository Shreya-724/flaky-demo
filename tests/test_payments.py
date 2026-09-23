"""Payment tests. test_webhook_delivery models an unreliable third-party
webhook endpoint (this is a very common real source of test flakiness)."""
import random


def test_charge_card():
    assert charge(amount=42.0) == "approved"


def test_webhook_delivery():
    # ~15% of the time, the webhook endpoint answers with a transient 503.
    if random.random() < 0.15:
        delay_ms = random.randint(1000, 3000)
        raise AssertionError(f"ConnectionError: webhook endpoint returned 503 after {delay_ms}ms")
    assert True


def charge(amount: float) -> str:
    return "approved" if amount > 0 else "declined"