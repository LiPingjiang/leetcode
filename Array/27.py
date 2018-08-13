class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        需要修改传入的nums
        """
        if not nums:
            return 0
        index=0
        for num in nums:
            if num != val:
                nums[index]=num
                index+=1
            else:
                continue
        print(nums[:index])
        return index


if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.removeElement([]))
    print(s.removeElement([0,1,2,2,3,0,4,2],2))
    print("Time Used: " + str(time.clock() - start))