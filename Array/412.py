class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret=[]
        for i in range(1,n+1):
            if i%3 == 0:
                if i%5 == 0:
                    ret.append('FizzBuzz')
                else:
                    ret.append('Fizz')
            elif i%5 == 0 :
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.maxRotateFunction( [4, 3, 2, 6] ))
    print(s.fizzBuzz( 15 ))
    print("Time Used: " + str(time.clock() - start))