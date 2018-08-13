class Solution:
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        s=sorted(set(nums))
        for n in s:
            nums[i]=n
            i+=1
        # print(nums)
        return len(s)
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        必要要修改输入数组nums
        """
        if not nums:
            return 0
        index=0
        for num in nums:
            if num == nums[index]:
                continue
            index+=1
            nums[index]=num
        # print(nums)
        return index+1


if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(s.removeDuplicates([]))
    # print(s.removeDuplicates([1,1,2]))
    print("Time Used: " + str(time.clock() - start))