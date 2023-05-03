from lessons.Exceptions import NotAListException


# Defining function to check if the length of the list is even
def is_list_even(input_string: list):
    # Check if input_string is a list
    if not isinstance(input_string, list):
        # Raise an exception if input_string is not a list
        return NotAListException('not a list')
    # Check if the length of the list is even
    return len(input_string) % 2 == 0
