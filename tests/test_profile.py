"""Profile tests. test_avatar_upload is deliberately, permanently broken (not
flaky) so the dashboard can show the difference: a consistently failing test
gets classified as "stable" (i.e. reliably broken), never "flaky"."""


def test_update_name():
    profile = {"name": "old"}
    profile["name"] = "new"
    assert profile["name"] == "new"


def test_avatar_upload():
    # Intentionally broken: the endpoint this hits was removed in a refactor
    # and nobody updated this test. Always fails, every run, every commit.
    raise AssertionError("HTTPError: 404 Not Found: /api/v1/avatar/upload (endpoint removed in #482)")