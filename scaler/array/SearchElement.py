def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = input()
    T = int(T)
    arr = []
    while(T>=1):
        N = input()
        for i in range(int(N)):
            num = input()
            arr.append(num)
        T = T - 1
        B = input()
    
        for i in range(int(N)):
            if arr[i] == B:
                print("YES Present")
    return 0

if __name__ == '__main__':
    main()