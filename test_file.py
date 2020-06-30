import pytest

x = 42
y = 3

def test_trivial():
	assert 1 == 1

@pytest.mark.slow
def test_2():
	assert y == 3

