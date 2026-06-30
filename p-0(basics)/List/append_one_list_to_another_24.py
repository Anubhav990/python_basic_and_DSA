def append_one_list_to_another(lst1, lst2):
    result = []
    
    for i in lst1:
        result.append(i)
        
    for j in lst2:
        result.append(j)
        
    return result

# def append_one_list_to_another(lst1, lst2):
#     return lst1 + lst2

if __name__ == "__main__":
    lst1 = list(input().split())
    lst2 = list(input().split())
    
    print(append_one_list_to_another(lst1, lst2))
    