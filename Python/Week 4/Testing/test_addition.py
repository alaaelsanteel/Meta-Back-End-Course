import addition
import pytest

def test_add():
    assert addition.add(4,5) == 9 #if it returns 9 then true

def test_sub():
    assert addition.sub(4,5) == -1
# to test write in terminal python -m pytest filename.py
# to run a specific func python -m pytest filename.py::funcName



