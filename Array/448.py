def setToNone(nums,idx):
    # print(nums,idx)
    if nums[idx-1] is not None:
        next=nums[idx-1]
        nums[idx-1]=None
        setToNone(nums,next)

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            if nums[i]:
                next=nums[i]
                # nums[i]=None
                setToNone(nums,next)
        ret=[]
        for i in range(0,len(nums)):
            if nums[i]:
                ret.append(i+1)
        return ret


    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret=[]
        for i in range(1,len(nums)+1):
            if nums.count(i)==0:
                ret.append(i)
        return ret

    def findDisappearedNumbers_fastest(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        不要在意什么不使用额外的空间。。。
        """
        marked = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in marked]


if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.findDisappearedNumbers( [4,3,2,7,8,2,3,1] ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))