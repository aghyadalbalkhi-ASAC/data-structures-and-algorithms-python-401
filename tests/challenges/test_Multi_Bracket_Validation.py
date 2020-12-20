from data_structures_and_algorithms.challenges.Multi_Bracket_Validation.Multi_Bracket_Validation import *



def test_Multi_Bracket_Validation_case1():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_Multi_Bracket_Validation_case2():
    actual = multi_bracket_validation('{}(){}')
    expected = True
    assert actual == expected

def test_Multi_Bracket_Validation_case3():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_Multi_Bracket_Validation_case4():
    actual = multi_bracket_validation('(){}[[]]')
    expected = True
    assert actual == expected

    
def test_Multi_Bracket_Validation_case5():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def test_Multi_Bracket_Validation_case6():
    actual = multi_bracket_validation('[({}]')
    expected = False
    assert actual == expected

def test_Multi_Bracket_Validation_case7():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def test_Multi_Bracket_Validation_case8():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected