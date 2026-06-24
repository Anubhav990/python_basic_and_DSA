import itertools

def generate_all_permutations_of_a_list(lst):
    perms = itertools.permutations(lst)
    return list(perms)

if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(generate_all_permutations_of_a_list(numbers)) 
      