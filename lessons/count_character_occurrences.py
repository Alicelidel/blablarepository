# Importing custom exceptions from Exceptions module
from lessons.Exceptions import NotAStringException, EmptyStringException


# Defining function to count the number of occurrences of a specific character in a string
def count_character_occurrences(input_string: str, character: str = "a") -> int:
    # Checking if input argument is a string
    if not isinstance(input_string, str):
        # Raising custom exception if argument is not a string
        raise NotAStringException("Not a string!")
    # Checking if input argument is an empty string
    if len(input_string) == 0:
        # Raising custom exception if argument is an empty string
        raise EmptyStringException("The string is empty")
    # Initializing counter to zero
    count = 0
    # Looping over each character in the input string
    for x in input_string:
        # If the current character is the specified character, increment the counter
        if x == character:
            count = count + 1
    # Returning the final count of occurrences of the specified character in the input string
    return count