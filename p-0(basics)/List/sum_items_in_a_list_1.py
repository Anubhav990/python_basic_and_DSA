def sum_all_items(lst):
    """
    This function takes a list of numbers as input and returns the sum of all the items in the list.
    :param lst: List of numbers
    
    """
    total = 0
    
    for num in lst:
        total += num
    return total

if __name__ == "__main__":
    
    numbers = list(map(int, input("Enter the numbers separated by spaces: ").split()))
    print("Sum of all items in the list:", sum_all_items(numbers))
    
    
    
    