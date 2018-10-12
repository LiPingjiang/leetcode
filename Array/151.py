class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # print(s.split(" "))
        # res=list(map(lambdda x: x.strip(), s.split(" ")))
        res= list(filter( lambda x: x!='', s.split(" ")))
        res.reverse()
        return " ".join(res).strip()

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.reverseWords( "   a   b " ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))