class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)+int(num2))

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.addStrings( [2, 2, 3, 1] ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))