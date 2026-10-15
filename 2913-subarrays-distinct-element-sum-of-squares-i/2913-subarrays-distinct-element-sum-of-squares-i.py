class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            temp = set()
            for j in range(i,len(nums)):
                if nums[j] not in temp:
                    temp.add(nums[j])
                    count+=1
                ans+=count*count
        return ans
