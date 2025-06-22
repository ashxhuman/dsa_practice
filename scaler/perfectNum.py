def main():
    """
    
    Given the Number of Test Cases as T,
    For each test case, take an integer N as input, you have to tell whether it is a perfect number or not.
    A perfect number is a positive integer that is equal to the sum of its proper positive divisors (excluding the number itself). 
    A positive proper divisor divides a number without leaving any remainder.
    
    """
    T = int(input())
    for x in range(T):
        N = int(input())
        sum = 0
        for i in range(1, N):
            if(N % i == 0):
                sum = sum + i
        if(sum == N):
            print("Yes")
        else:
            print("No")
    return 0

if __name__ == '__main__':
    main()