def access_index_in_a_list(lst):
    result = []
    for index, value in enumerate(lst):
        result.append((index, value))
    return result

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(access_index_in_a_list(numbers))
    
    