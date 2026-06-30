def find_second_smallest_number_in_list_27(lst):
    smallest = float('inf')
    second_smallest = 0
    
    for i in lst:
        if (i < smallest):
            second_smallest = smallest
            smallest = i
        elif (smallest < i < second_smallest):
            second_smallest = i
    return second_smallest

if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(find_second_smallest_number_in_list_27(lst))
    
    