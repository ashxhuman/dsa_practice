def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    arr = []
    for i in range(N):
        num = input()
        arr.append(num)

    min_val, max_val = arr[0], arr[0]
    for i in range(N):
        for j in range(N):
            if arr[i]>arr[j] and i!=j:
                if arr[j]>max_val:
                    max_val=arr[j]
                if arr[i]<min_val:
                    min_val=arr[i] 
    return 0

if __name__ == '__main__':
    main()