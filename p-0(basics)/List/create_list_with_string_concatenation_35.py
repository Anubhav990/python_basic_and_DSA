def list_with_string_concatenation(lst, n):
    new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in lst]
    return new_list

if __name__ == "__main__":
    my_list = list(input().split())
    n = int(input())
    print(list_with_string_concatenation(my_list, n))
    