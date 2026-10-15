class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            temp = []
            for j in range(i,len(nums)):
                if nums[j] not in temp:
                    temp.append(nums[j])
                    count+=1
                ans+=count*count
        return ans
