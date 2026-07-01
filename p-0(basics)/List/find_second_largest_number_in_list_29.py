def find_second_largest_number(lst):
    largest = float('-inf')
    second_largest = 0
    
    for i in lst:
        if (i > largest):
            second_largest = largest
            largest = i
        elif (largest > i > second_largest):
            second_largest = i
    return second_largest

if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(find_second_largest_number(lst))