def prime_number_sieve_of_ethiosis(n):
    
    primes = []
    
    for i in range(2, n + 1):
        if i not in primes:
            
            print(i)
            
            for j in range(i * i, n + 1, i):
                primes.append(j)
                
    
if __name__ == "__main__":
    n = int(input())
    prime_number_sieve_of_ethiosis(n)
            