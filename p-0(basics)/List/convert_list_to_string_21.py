
def convert_list_to_string(lst):
    str1 = ''.join(lst)
    return str1

if __name__ == "__main__":
    sample_list = list(input().split())
    print(convert_list_to_string(sample_list))