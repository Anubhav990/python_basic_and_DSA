def difference_between_two_lists(lst1, lst2):
    diff_list1_list2 = list(set(lst1) - set(lst2))
    
    diff_list2_list1 = list(set(lst2) - set(lst1))
    
    total_diff = (diff_list1_list2 + diff_list2_list1)
    return total_diff

if __name__ == "__main__":
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    
    print(difference_between_two_lists(lst1, lst2))    