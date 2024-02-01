import math

def reading_time_estimator(text, wpm):
    if not isinstance(text, str):
        raise Exception("Value given for text argument must be a string")
    
    if not isinstance(wpm, (int, float)):
        raise Exception("Value given for wpm argument was invalid")
    
    if text == "" or text == " ":
        raise Exception("No string inputted - cannot estimate reading time for an empty string")

    words_in_text = len(text.split())
    time_in_seconds = math.ceil((words_in_text/wpm)*60)
    time_in_minutes = math.floor(words_in_text/wpm)
    if time_in_seconds >= 60:
        time_in_seconds_formatted = time_in_seconds % 60
        return f"Esitated reading time is {time_in_minutes} minutes and {time_in_seconds_formatted} seconds"
    else:
        return f"Esitated reading time is {time_in_minutes} minutes and {time_in_seconds} seconds"

