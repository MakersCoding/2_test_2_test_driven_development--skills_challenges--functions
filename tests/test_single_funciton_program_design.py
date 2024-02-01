from lib.single_funciton_program_design import reading_time_estimator
import pytest

"""
Given a small and evenly divisible (at 200 wpm) string of text 
"one tow three four five six seven eight nine ten"
returns the estimated time for the user to read all the words
"""

def test_reading_time_for_small_evenly_divisible_string():
    result = reading_time_estimator("one tow three four five six seven eight nine ten", 200)
    assert result == "Esitated reading time is 0 minutes and 3 seconds"

"""
Given a large and evenly divisible (at 200 wpm) string of text 
returns the estimated time for the user to read all the words in minutes and seconds
"""

def test_reading_time_for_large_evenly_divisible_string():
    result = reading_time_estimator("""
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World

""", 200)
    assert result == "Esitated reading time is 1 minutes and 6 seconds"

"""
Given a large and uneven string, the result must be rounded (235 words)
returns the estimated time for the user to read all the words
"""

def test_reading_time_for_large_not_evenly_divisible_string():
    result = reading_time_estimator("""
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello World
Hello World Hello World Hello World Hello World Hello World Hello World Hello World Hello 
""", 200)
    assert result == "Esitated reading time is 1 minutes and 11 seconds"

"""
Tests to ensure if the WPM value given is a float, the test will still function

"""

def test_reading_time_for_wpm_float():
    result = reading_time_estimator("one two three four five six seven eight nine ten", 2.156)
    assert result == "Esitated reading time is 4 minutes and 39 seconds"

"""
Given a iterable that is not a string for the "text" argument
returns an error to the user
"""

def test_reading_time_text_argument_not_a_string():
    with pytest.raises(Exception) as err:
        reading_time_estimator([27], 200)
    error_message = str(err.value)
    assert error_message == "Value given for text argument must be a string"

"""
Given a iterable that is not a integer or float for the "wpm" argument
returns an error to the user
"""

def test_reading_time_wpm_argument_not_a_int_or_float():
    with pytest.raises(Exception) as err:
        reading_time_estimator("", [])
    error_message = str(err.value)
    assert error_message == "Value given for wpm argument was invalid"


"""
Given an empty string (no text) 
rasies an error: "No string inputted - cannot estimate reading time for an empty string"
"""

def test_reading_time_for_empty_string_raises_error():
    with pytest.raises(Exception) as err:
        reading_time_estimator("", 200)
    error_message = str(err.value)
    assert error_message == "No string inputted - cannot estimate reading time for an empty string"