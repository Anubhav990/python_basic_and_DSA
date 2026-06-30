def check_whether_two_lists_are_circularly_identical(lst1, lst2):
    
    return (''.join(map(str, lst2)) in ''.join(map(str, lst1 * 2)))

if __name__ == "__main__":
    lst1 = list(input().split())
    lst2 = list(input().split())
    
    print(check_whether_two_lists_are_circularly_identical(lst1, lst2))
    