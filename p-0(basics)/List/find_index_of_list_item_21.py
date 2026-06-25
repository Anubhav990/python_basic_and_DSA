def find_index_of_list_item(lst, n):
    result = lst.index(n)
    return result

if __name__ == "__main__":
    sample_list = list(map(int, input().split()))
    n = int(input())
    print(find_index_of_list_item(sample_list, n))