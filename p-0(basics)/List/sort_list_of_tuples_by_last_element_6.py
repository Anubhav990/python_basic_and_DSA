# def sort_list_of_tuples_by_last_element(lst):
    
#     """
#     This function sorts the tuples in the list according to their last values and returns the new list
#     param lst: list of tuples
    
#     """
    
#     n = len(lst)
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             if lst[i][-1] > lst[j][-1]:
#                 temp = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = temp
#     return lst

# another sorted function method
def last(n):
    return n[-1]
    
    
def sort_list_last(tuples):
    return sorted(tuples, key=last)
    

if __name__ == "__main__":
    
    n = int(input("Enter the number of tuples: "))
    
    t = []
    tuple_count = 1
    
    for i in range(n):
        
        val = input(f"Enter space separated values for tuple {tuple_count}: ").split()
        tuple_count += 1
        t.append(tuple(map(int, val)))
        
    # print(sort_list_of_tuples_by_last_element(t))
    print(sort_list_last(t))