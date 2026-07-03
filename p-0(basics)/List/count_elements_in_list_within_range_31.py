def count_elements_in_range(lst, lower_bound, upper_bound):
    count = 0
    for i in lst:
        if (lower_bound <= i <= upper_bound):
            count += 1
    return count

if __name__ == "__main__":
    lst = list(input().split())
    lower_bound = input()
    upper_bound = input()
    print(count_elements_in_range(lst, lower_bound, upper_bound))