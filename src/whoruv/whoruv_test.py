from whoruv.whoruv import whoruv


def test_whoruv() -> None:
    assert whoruv() == "Hello!"
