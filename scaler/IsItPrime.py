def main():
    num = int(input())
    # flag = "NO"
    # if num <= 1:
    #     print(flag)
    # else:
    #     for x in range(2, int(num**0.5)+1):
    #         if(num % x == 0):
    #             print(flag)
    #             break
    #         else:
    #             continue
    #     flag = "YES"
    #     print(flag)
    for x in range(2,num):
        if(num % x==0):
            print("NO")
            break
        else:
            print("Yes")
    return 0

if __name__ == '__main__':
    main()
