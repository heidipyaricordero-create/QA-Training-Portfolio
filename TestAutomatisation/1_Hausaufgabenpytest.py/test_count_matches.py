import pytest
from count_word_matches import count_word_matches

@pytest.mark.parametrize("a,b, expected",[
    ("The cat sat on the mat", "cat", 1), 
    ("Dog dog DOG dOg", "dog", 4),
    ("Hello world", "world", 1),
    ("hello hello HELLO", "hello", 3),
    ("No matches here", "yes", 0),
    ("catcat cat catdog", "cat", 1),
    ("a a a", "a", 3)
    ])

def test_count_word_matches_parametrise(a, b, expected):
    """
    Test the function with a variety of string patterns and word counts.
    Verifies case-insensitive matching and ensures that partial 
    word matches (like 'catdog') are correctly excluded.
    """
    assert count_word_matches(a, b) == expected



def test_count_word_matches_edge_case_testing():
    """
    Test edge cases such as empty strings and white space handling.
    Ensures that empty inputs return 0 and specific word boundaries 
    are correctly identified.
    """
    assert count_word_matches("", "word") == 0
    assert count_word_matches("hello world", "") == 0
    assert count_word_matches("", "") == 0
    assert count_word_matches("hello world", "world") == 1
    assert count_word_matches(" cat " , "cat") == 1
    assert count_word_matches("cat,dog cat", "cat") == 1
    assert count_word_matches("x y z", "x") == 1


def test_count_word_matches_negative_testing():
    """
    Test the function's behavior with invalid input types.
    Ensures that None values return 0 and incorrect data types 
    properly raise an AttributeError.
    """
    assert count_word_matches(None, "word") == 0
    assert count_word_matches("hello world", None) == 0
    with pytest.raises(AttributeError):
         count_word_matches(123, "word")
    with pytest.raises(AttributeError):
        count_word_matches("hello world", 456)
    with pytest.raises(AttributeError):
        count_word_matches(["hello", "world"], "world")
    with pytest.raises(AttributeError):
        count_word_matches("hello world", ["world"])
