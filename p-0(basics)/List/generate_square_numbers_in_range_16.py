def print_values():
    squares = []
     
    for i in range(1, 21):
        squares.append(i ** 2)
        
    print(squares[:5])
    print(squares[5:]) 

if __name__ == "__main__":
    print_values()
    