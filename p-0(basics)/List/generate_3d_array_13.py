def generate_3d_array(x, y, z):
    
     """
    This function takes a dimension of numbers as input and returns a 3D array
    :param lst: numbers of different dimensions 
    
    """
    
    return [[['*' for k in range(z)] for j in range(y)] for i in range(x)]

if __name__ == "__main__":
    x = int(input("Enter size for dimension 1 : "))
    y = int(input("Enter size for dimension 2 : "))
    z = int(input("Enter size for dimension 3 : "))
    
    array = generate_3d_array(x, y, z)
    
    for i in range(x):
        print(f"Layer {i}:")
        for j in range(y):
            print(array[i][j])
        print()
    