class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(0, len(nums)):
            freq[nums[i]] += 1
        
        freqKeys = list(freq.keys())
        freqKeys = sorted(freqKeys, key=freq.get)
        return freqKeys[-k:]
 

