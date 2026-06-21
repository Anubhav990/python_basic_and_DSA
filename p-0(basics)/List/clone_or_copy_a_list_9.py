# Manual copy without any built in methods

def clone_a_list(lst):
    result = []
    for i in lst:
        result.append(i)
    return result

if __name__ == "__main__":
    numbers = list(map(int, input("Enter space separated integers : ").split()))
    print(clone_a_list(numbers))
    

#Deep copy code

# import copy

# def clone_a_list(lst):
#     deep_copy = copy.deepcopy(lst)
#     return deep_copy

# if __name__ == "__main__":
#     numbers = list(map(int, input("Enter space separated integers : ").split()))
#     print(clone_a_list(numbers))