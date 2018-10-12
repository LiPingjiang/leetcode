class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(set(nums))[-3] if len(set(nums))>=3 else max(nums)

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.thirdMax( [2, 2, 3, 1] ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))