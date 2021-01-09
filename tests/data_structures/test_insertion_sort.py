from data_structures_and_algorithms.data_structures.sorting_algorithms.insertion_sort import insertionSort
import pytest

def test_empty_case(): 
    arr = [10,77,23,55,2]
    assert insertionSort(arr) == [2,10,23,55,77]