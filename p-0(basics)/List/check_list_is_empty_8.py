def check_if_list_empty(lst):
    
    """
    This function takes a list of numbers as input and returs if the list is empty or not.
    :param lst: List of numbers
    
    """
    
    if len(lst) == 0:
        return "List is Empty"
    return "List is not Empty"

if __name__ == "__main__":
    numbers = list(map(int, input("Enter the values with space separated integers : ").split()))
    print(check_if_list_empty(numbers))
    