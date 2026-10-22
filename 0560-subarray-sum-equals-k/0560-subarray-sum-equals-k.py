class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        pre=count=0

        for i in nums:
            pre+=i
            need = pre - k
            if need in seen:
                count+=seen[need]
            seen[pre] = seen.get(pre,0)+1
        return count