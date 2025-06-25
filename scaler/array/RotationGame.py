def main():
    N = int(input())
    A = [N]
    for i in range(N-1):
        num = input()
        A.push(num)
    B = int(input())
    reverse(A, 0, B-1)
    reverse(A, B, N-1)
    reverse(A, 0, N)
    print(A)

def reverse(arr, start, end):
    i=start
    j=end
    while(i<j): 
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i = i+1
        j = j-1

if __name__ == 'main':
    main()