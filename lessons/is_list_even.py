from lessons.Exceptions import NotAListException


# Defining function to check if the length of the list is even
def is_list_even(input_list: list):
    # Check if input_string is a list
    if not isinstance(input_list, list):
        # Raise an exception if input_string is not a list
        return NotAListException('not a list')
    # Check if the length of the list is even
    return len(input_list) % 2 == 0
