class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.


        a[start:end] # items start through end-1
        a[start:]    # items start through the rest of the array
        a[:end]      # items from the beginning through end-1
        a[:]         # a copy of the whole array
        a[start:end:step] # start through not past end, by step

        The key point to remember is that the :end value represents the first value that is not in the selected slice. So, the difference beween end and start is the number of elements selected (if step is 1, the default).
        The other feature is that start or end may be a negative number, which means it counts from the end of the array instead of the beginning. So:

        a[-1]    # last item in the array
        a[-2:]   # last two items in the array
        a[:-2]   # everything except the last two items

        Similarly, step may be a negative number:

        a[::-1]    # all items in the array, reversed
        a[1::-1]   # the first two items, reversed
        a[:-3:-1]  # the last two items, reversed
        a[-3::-1]  # everything except the last two items, reversed

        list = ['a', 'b', 'c', 'd']
        print list[1:-1]   ## ['b', 'c']
        list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
        print list         ## ['z', 'c', 'd']

        """
        l=len(nums)
        k=k%l
        if k != 0:
            nums[:]=nums[-k:]+nums[:(l-k)]
        return nums
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        nums_cp=nums.copy()
        for i in range(0,l):
            nums[i]=nums_cp[((i-k)+l)%l]
        return nums

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.rotate( [1,2,3,4,5,6,7],3))
    print("Time Used: " + str(time.clock() - start))