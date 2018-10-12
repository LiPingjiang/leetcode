class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target=len(nums)/2
        for i in set(nums):
            if nums.count(i)> target:
                return i

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.maxProfit([7,1,5,3,6,4]))
    print(s.majorityElement([3,2,3]))
    print("Time Used: " + str(time.clock() - start))