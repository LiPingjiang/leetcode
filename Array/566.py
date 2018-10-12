class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        items=[]
        for row in nums:
            for item in row:
              items.append(item)
        print(items)
        if len(items) != r*c:
            return nums
        ret=[]
        for i in range(0,r):
            ret.append([])
            for j in range(0,c):
                ret[i].append(items[i*c+j])
        return ret


    def matrixReshape_fastest(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        from itertools import chain
        m = len(nums)
        n = len(nums[0])
        # ilegal
        if m*n != r*c:
            return nums
        # # row reshape
        # arr = []
        # for i in range(r):
        #     temp = []
        #     for j in range(c):
        #         pos = c*i+j
        #         # original position
        #         p = pos//n
        #         q = pos%n
        #         temp.append(nums[p][q])
        #     arr.append(temp)

        # super fast
        generator = chain.from_iterable(nums) # to 1D array
        repeator = [generator]*c # repeat the same generator c times => read c values at the same time
        arr = list(zip(*repeator))

        # super fast understandable
        # def generator():
        #     for i in range(m):
        #         for j in range(n):
        #             yield nums[i][j]


        return arr

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.matrixReshape( [[1,2], [3,4]] , 2, 4 ))
    # print(s.matrixReshape( [[1,2], [3,4]] , 1, 4 ))
    print(s.matrixReshape_fastest( [[1,2,3,4]], 2, 2 ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))