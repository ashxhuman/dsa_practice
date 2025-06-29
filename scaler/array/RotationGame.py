def main():
    print("#################")
    N = int(input())
    A = []
    for i in range(N):
        num = input()
        A.append(num)
    B = int(input())
    B = B % N
    reverse(A, 0, N-1)
    reverse(A, 0, B-1)
    reverse(A, B, N-1)
    print("##################")
    for j in range(N):
        print(A[j])
    return 0

def reverse(arr, start, end):
    i=int(start)
    j=int(end)
    while(i<j): 
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i = i+1
        j = j-1

if __name__ == '__main__':
    main()