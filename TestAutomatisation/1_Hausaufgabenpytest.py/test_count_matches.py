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

    assert count_word_matches(a, b) == expected


@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),                
    ("hello world", "", 0),         
    ("", "", 0),                    
    ("hello   world", "world", 1),   
    ("  cat  ", "cat", 1),          
    ("cat,dog cat", "cat", 1),      
    ("x y z", "x", 1),              
])

def test_count_words_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected



def test_count_word_matches_negative_testing():

    
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
