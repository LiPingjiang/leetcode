class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for num in nums:
        #     if (num >= target):
        #         continue
        #     index=nums.index(num)
        #     if num*2 == target and num in nums[index+1:]:
        #         return [index, index+nums[index+1:].index(num)]
        #     if ( target-num ) in nums :
        #         return [nums.index(num),nums.index(target-num)]
        for index,num in enumerate(nums):
            print(num,nums[index+1:])
            if num*2 == target and num in nums[index+1:]:
                return [index, 1+index+nums[index+1:].index(num)]
            if ( target-num ) in nums[index+1:] :
                return [index,nums.index(target-num)]
        return []

if __name__ == '__main__':
    s=Solution()
    # print(s.twoSum([3,2,4],6))
    # print(s.twoSum([3,3],6))
    print(s.twoSum([0,4,3,0],0))
