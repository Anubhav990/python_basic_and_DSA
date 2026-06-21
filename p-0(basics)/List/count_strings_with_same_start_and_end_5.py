def count_strings_with_same_start_and_end(lst):
    
    """
    This function takes a list of strings as input and returns the count of strings that have the same first and last character.
    :param lst: List of strings
    
    """
    count = 0
    for val in lst:
        if (len(val) >= 2 and val[0] == val[-1]):
            count += 1
    return count

if __name__ == "__main__":
    
    list_of_strings = input("Enter the values separated by spaces ").split()
    print("Count of strings with same start and end:", count_strings_with_same_start_and_end(list_of_strings))