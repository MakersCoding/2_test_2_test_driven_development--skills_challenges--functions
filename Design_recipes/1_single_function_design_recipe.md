# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

- estimate so doesn't have to be exact
- simple mathemartial equasaion
- Breaks should not be accounted for as assumption is made that the block of text is small and read in one go. 
## 2. Design the Function Signature
_Include the name of the function, its parameters, return value, and side effects._

```python 

def reading_time_estimator(text, wpm)
    """
    Extracts the given text and words per minute (wpm)
    calculates the estmated time it will take the user to read the text in minutes 
    
    Parameters:
    text = The input text given by the user 
    wpm = Words per minute provided by the user 

    Returns: The estiamted time it will take the user to read the given text in minutes and seconds (rounded up to nearest second) provided as an easy to read string.

    Side effects: None foreseen at the time of writing
    """
    pass 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a small and evenly divisible (at 200 wpm) string of text 
"one tow three four five six seven eight nine ten"
returns the estimated time for the user to read all the words
"""
reading_time_estimator("one tow three four five six seven eight nine ten", 200) => "Esitated reading time is 0 minutes and 3 seconds"

"""
Given a larger string of text (220 words)
returns the estimated time for the user to read all the words
"""

reading_time_estimator("""
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

""", 200) => "Esitated reading time is 1 minutes and 6 seconds"

"""
Given a large and uneven string so the result must be rounded (235 words)
returns the estimated time for the user to read all the words
"""
reading_time_estimator("""
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


""", 200) => "Esitated reading time is 1 minutes and 11 seconds"

"""
Tests to ensure if the WPM value given is a float, the test will still function

"""

reading_time_estimator("one two three four five six seven eight nine ten", 2.156) => "Esitated reading time is 4 minutes and 39 seconds"


"""
Given a iterable that is not a string for the "text" argument
returns an error to the user
"""

reading_time_estimator([27], 200) => "Error: Value given for text argument must be a string"

"""
Given a iterable that is not a integer or float for the "wpm" argument
returns an error to the user
"""

reading_time_estimator("", []) => "Error:  Value given for wpm argument was invalid"

"""
Given an empty string (no text) 
returns a time of 0 minutes and 0 seconds 
"""
reading_time_estimator("", 200) => "No string inputted - cannot estimate reading time for an empty string"



```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

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
    
```

Ensure all test function names are unique, otherwise pytest will ignore them!