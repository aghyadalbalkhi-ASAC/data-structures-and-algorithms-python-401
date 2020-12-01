import pytest
# from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray 
from data_structures_and_algorithms.challenges.binary_search.binary_search import *

def test_array_binarySearch():
    array = [ 25, 35, 65, 80, 85,86,96,97,98,102,111 ] 
    target = 96
    actual = array_binarySearch(array,target)
    expected = 6
    assert actual == expected