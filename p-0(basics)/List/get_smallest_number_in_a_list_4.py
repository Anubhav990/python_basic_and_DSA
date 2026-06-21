def smallest_number_in_list(lst):
    
    """
    This function take a list of numbers as input and returns the smallest number in the list.
    :param lst: List of numbers
    
    """
    min_value = float("inf")
    
    for num in lst:
        if (num < min_value):
            min_value = num
    return min_value

if __name__ == "__main__":
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    print("Smallest number in the list: ", smallest_number_in_list(numbers))
    
    