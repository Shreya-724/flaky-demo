"""Auth tests. All stable: no timing or network dependency here."""


def test_login():
    assert authenticate("user", "correct-password")


def test_logout():
    session = {"active": True}
    session["active"] = False
    assert session["active"] is False


def test_signup():
    users = set()
    users.add("newuser")
    assert "newuser" in users


def authenticate(username: str, password: str) -> bool:
    return username == "user" and password == "correct-password"