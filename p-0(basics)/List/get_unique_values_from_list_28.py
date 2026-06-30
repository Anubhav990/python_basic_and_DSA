def get_unique_values_from_list(lst):
    custom_set = set(lst)
    final_lst = list(custom_set)
    
    return final_lst

if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(get_unique_values_from_list(lst))