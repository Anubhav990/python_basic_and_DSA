def largest_number_in_list(lst):
    
    """
    This function takes a list of numbers as input and returns the largest number in the list.
    :param lst: List of numbers
    
    """
    
    max_value = float("-inf")
    
    for num in lst:
        if num  > max_value:
            max_value = num
            
    return max_value

if __name__ == "__main__":
    
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    
    print("Largest number in the list:", largest_number_in_list(numbers))
    