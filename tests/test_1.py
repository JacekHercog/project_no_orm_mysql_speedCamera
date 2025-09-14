import pytest

@pytest.mark.integration
def test_database_connection():
    # Real database test
    pass

def test_1():
    assert isinstance(1, int)