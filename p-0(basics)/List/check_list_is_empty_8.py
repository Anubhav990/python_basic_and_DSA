def check_if_list_empty(lst):
    if len(lst) == 0:
        return "List is Empty"
    return "List is not Empty"

if __name__ == "__main__":
    numbers = list(map(int, input("Enter the values with space separated integers : ").split()))
    print(check_if_list_empty(numbers))
    