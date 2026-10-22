class Solution:
    def left(self, nums: List[int]):
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
        
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = nums.index(0)
        #check ascending order from zero position
        if all(nums[(z+i)%n] == i for i in range(n)):
            # check rotate by left ring cost vs right ring and give it's min
            return min(z,n-z+2)
        # similarly for descending
        if all(nums[(z-i)%n] == i for i in range(n)):
            return min(n-z,z+2)
        return -1