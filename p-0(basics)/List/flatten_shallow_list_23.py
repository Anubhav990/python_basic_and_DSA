def flatten_shallow_list(lst):
    flat = []
    
    for sublist in lst:
        for item in sublist:
            flat.append(item)
            
    return flat

if __name__ == "__main__":
    lst = eval(input("Enter a shallow nested list :"))
    print(flatten_shallow_list(lst))
     
    