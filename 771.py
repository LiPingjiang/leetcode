class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=dict()
        result=0
        for s in S:
            count[s]=count.get(s, 0)+1
        for j in J:
            result+=count.get(j, 0)
        return result


if __name__ == '__main__':
    s=Solution()
    # print(s.twoSum([3,2,4],6))
    # print(s.twoSum([3,3],6))
    print(s.numJewelsInStones('aA',"aAAbbbb"))
