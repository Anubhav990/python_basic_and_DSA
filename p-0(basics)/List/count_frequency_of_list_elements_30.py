import collections

def count_frequency(lst):
    ctr = collections.Counter(lst)
    
    return ctr

if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(count_frequency(lst))
    