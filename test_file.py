import pytest

x = 42
y = 3

def test_trivial():
	assert 1 == 1

@pytest.mark.slow
def test_2():
	# give this code some more volume
	bla = 5
	bla *= 1
	assert y == 3

def spam_function():
	# this only exists to test what happens
	return 0