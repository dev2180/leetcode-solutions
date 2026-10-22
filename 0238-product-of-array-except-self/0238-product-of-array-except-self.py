class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #expand around the center
        # n = len(nums)
        # left = [1]*n
        # right = [1]*n

        # for i in range(1,n):
        #     left[i] = left[i-1]*nums[i-1]

        # for i in range(n-2,-1,-1):
        #     right[i] = right[i+1]*nums[i+1]
        
        # return [left[i]*right[i] for i in range(n)]

        n = len(nums)
        res = [1]*n
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
        r = 1
        for j in range(n-1,-1,-1):
            res[j] *=r
            r*=nums[j]
        return res 