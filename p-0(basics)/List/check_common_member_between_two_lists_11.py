def check_common_member_between_two_lists(lst1, lst2):
    
    """
    This function takes two lists of numbers as input and returns True if there is a common member between the two lists.
    :param lst: 2 Lists of numbers
    
    """
    result = False
    
    for i in lst1:
        for j in lst2:
            if (i == j):
                return True
    return result

if __name__ == "__main__":
    lst1 = list(map(int, input("Please Enter numbers separated by a space : ").split()))
    lst2 = list(map(int, input("Please Enter numbers separated by a space : ").split()))
    print(check_common_member_between_two_lists(lst1, lst2))
    