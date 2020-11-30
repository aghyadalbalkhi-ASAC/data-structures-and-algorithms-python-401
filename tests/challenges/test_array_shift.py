import pytest
# from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray 
from data_structures_and_algorithms.challenges.array_shift.array_shift import *

def test_insertShiftArray():
    actual = insertShiftArray([4,8,15,23,42],16)
    expected = [4,8,15,16,23,42]
    assert actual == expected