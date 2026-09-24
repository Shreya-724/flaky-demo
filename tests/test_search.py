"""Search tests. test_results_load_in_time is the flakiest test in this repo,
simulating a page that sometimes takes longer than the client's timeout."""
import random


def test_basic_query():
    results = ["a", "b", "c"]
    assert len(results) == 3


def test_results_load_in_time():
    # ~25% of the time, results take longer than the UI's wait timeout.
    if random.random() < 0.25:
        wait_ms = random.randint(4000, 6000)
        raise AssertionError(f"Timeout after {wait_ms}ms waiting for #results")
    assert True