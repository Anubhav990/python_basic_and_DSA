def print_format_id(custom_var, custom_str):
    return format(id(custom_var), custom_str)

if __name__ == "__main__":
    my_var = input()
    print(print_format_id(my_var, "x"))