import pytest

x = 42

def test_trivial():
	assert 1 == 1

def test_variable():
	assert x == 42
