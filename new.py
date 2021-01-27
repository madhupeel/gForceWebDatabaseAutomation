import pytest

@pytest.mark.usefixtures()
def test_adding(add):
    assert add(2, 3) == 5
    print 5