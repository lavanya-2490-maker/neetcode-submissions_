class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            freq[i]+=1
        for key in freq:
            if freq[key]>2:
                return True
        return False
        