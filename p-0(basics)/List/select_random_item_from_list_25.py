import random

def select_random_item_from_list(lst):
    result = random.choice(lst)
    
    return result

if __name__ == "__main__":
    lst = list(input().split())
    print(select_random_item_from_list(lst))