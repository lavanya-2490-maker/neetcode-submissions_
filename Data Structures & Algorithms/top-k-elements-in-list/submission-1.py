class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        arr=sorted(freq,key=freq.get,reverse=True)
        return arr[:k]
        