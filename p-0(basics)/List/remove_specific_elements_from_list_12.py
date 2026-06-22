def remove_specific_elements_from_list(lst1, lst2):
    
     """
    This function takes two list of numbers as input and returns the removed values from the first list with respect to the input from the second list.
    :param lst: Lists of numbers
    
    """
    
    result = []
    
    for i in range (len(lst1)):
        if i not in lst2:
            result.append(lst1[i])
    return result
    

if __name__ == "__main__":
    lst = list(input("Enter The Sentence : ").split())  #split will split the sentence into words not characters
    indices = list(map(int, input("Enter space separated integers : ").split()))
    print(remove_specific_elements_from_list(lst, indices))