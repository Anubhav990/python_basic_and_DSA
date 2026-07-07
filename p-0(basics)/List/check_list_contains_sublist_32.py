def is_sublist(lst, sub):
    #edge case
    
    if sub == []:
        return True

    if sub == lst:
        return True
    
    if (len (sub) > len(lst)):
        return False
    
    #check every possible starting position
    
    for i in range(len(lst) - len(sub) + 1):
        
        #first element matches
        if (lst[i] == sub[0]):
            n = 1
            
            #check the remaining elements
            while (n < len(sub) and lst[i + n] == sub[n]):
                n += 1  
                
            #Entire sublist matched
            if (n == len(sub)):
                return True
    return False
    
if __name__ == "__main__":
    main_list = list(map(int, input().split()))
    sub_list = list(map(int, input().split()))
    
    if is_sublist(main_list, sub_list):
        print("True")
    else:
        print("False")
        