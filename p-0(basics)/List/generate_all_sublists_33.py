from itertools import combinations

def sub_lists(lst):
    sublist = []
    
    for i in range(0, len(lst) + 1):
        
        temp = [list(x) for x in combinations(lst, i)]
        
        if (len(temp) > 0):
            sublist.extend(temp)
            
    return sublist

if __name__ == "__main__":
    lst = list(input().split())
    print(sub_lists(lst))