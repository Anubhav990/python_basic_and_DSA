def remove_duplicates_from_list(lst):
    # result = []
    
    # for i in range(len(lst)):
        
    #     is_duplicate = False #keep a flag
        
    #     for j in range(i + 1, len(lst)):
    #         if (lst[i] == lst[j]):
    #             is_duplicate = True
    #             break
    #     if not is_duplicate:
    #         result.append(lst[i])
                
    # return result
    
    """
    This function takes a list of numbers as input and returns if there are any duplicates inside the list.
    :param lst: List of numbers
    
    """
    
    seen = set()
    result = []
    
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result
        
                
if __name__ == "__main__":
    numbers = list(map(int, input("Print space separated integers : ").split()))
    print(remove_duplicates_from_list(numbers))