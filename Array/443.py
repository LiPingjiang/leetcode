class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res=""+chars[0]
        i=1
        count = 1
        while(i<len(chars)):
            if chars[i] == res[-1]:
                count+=1
            else:
                if count != 1:
                    res+=str(count)
                res+=chars[i]
                count=1
            i+=1
        if count != 1:
            res+=str(count)
        for i in range(0,len(res)):
            chars[i]=res[i]
        return len(res)

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.compress( ["a","b","b","b","b","b","b","b","b","b","b","b","b"] ))
    # print(s.thirdMax( [3,2,1] ))
    # print(s.thirdMax( [1,2] ))
    print("Time Used: " + str(time.clock() - start))