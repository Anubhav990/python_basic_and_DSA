from random import shuffle 

def shuffler(lst):
    
    """
    This function takes a list and shuffles it values
    :param lst: List of numbers or string
    
    """

    shuffle(lst)
    return lst

if __name__ == "__main__":
    lst = list(input().split())
    print(shuffler(lst))
    
    