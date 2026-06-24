def is_prime(n):
    
    if (n == 1):
        return False
    elif(n == 2):
        return True
    else:
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True
    
def check_if_all_numbers_are_prime(numbers):
    for num in numbers:
        if not is_prime(num):
            return False
    return True
            


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(check_if_all_numbers_are_prime(numbers))
    