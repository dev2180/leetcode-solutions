class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[0:k])
        l,n = 0,len(nums)
        m_val = cur_sum/k
        for i in range(k,n):
            cur_sum=cur_sum-nums[l]+nums[i]
            l+=1
            m_val = max(m_val,cur_sum/k)
        return m_val
