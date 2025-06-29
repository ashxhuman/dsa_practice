class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        N = len(A)
        for i in range(N):
            for j in range(i+1, N):
                if A[i]+A[j]==B and i!=j:
                    count += 1
        
        return count


# Create an instance
s = Solution()

# Call the method using the instance
p1 = s.solve(A=[1,2,2], B=4)
print(p1)