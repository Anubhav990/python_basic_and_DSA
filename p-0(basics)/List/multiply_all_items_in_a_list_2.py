def multiply_all_items(lst):
    """
    This function takes a list of numbers as input and returns the product of all the items in the list.
    :param lst: List of numbers
    
    """
    product = 1
    
    for num in lst:
        product *= num
    return product

if __name__ == "__main__":
    
    numbers = list(map(int, input("Enter the numbers separated by spaces:").split()))
    print("Product of all items in a list:", multiply_all_items(numbers))