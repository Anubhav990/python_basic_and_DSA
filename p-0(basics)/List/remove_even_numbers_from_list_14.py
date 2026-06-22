def remove_even_numbers_from_list(lst):
    
    """
    This function takes a list of numbers as input removes the even numbers and returns the list with all the odd integers
    :param lst: List of numbers
    
    """
    
    result = []
    
    for i in lst:
        if (i % 2 != 0):
            result.append(i)
            
    return result
            

if __name__ == "__main__":
    
    numbers = list(map(int, input("Enter the space separated numbers : ").split()))
    print(remove_even_numbers_from_list(numbers))