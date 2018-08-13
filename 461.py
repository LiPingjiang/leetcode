class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print( bin(x) )
        # print( bin(y) )
        bx=bin(x)[2:]
        by=bin(y)[2:]
        print("bx="+bx)
        print("by="+by)
        lx=len(bx)
        ly=len(by)
        difs=''
        minl=min(lx,ly)
        count=0
        if lx > ly:
            difs=bx[0:lx-minl]
            bx=bx[-ly:]
        else:
            difs=by[0:ly-minl]
            by=by[-lx:]
        print("bx="+bx)
        print("by="+by)
        print("difs="+difs)
        print("minl="+str(minl))

        for i in range(0,minl):
            # print(i)
            if bx[i]!=by[i]:
                count+=1
        print('count= ' + str(count))
        return count+difs.count('1')


        # return result
    def hammingDistance_fastest(self, x, y):
        print('x= '+str(x))
        print('y= '+str(y))
        print('x^y= '+ str(x^y))# ^     按位异或运算符：当两对应的二进位相异时，结果为1
        print('bin(x^y)= '+ bin(x^y))
        return bin(x^y).count('1')


if __name__ == '__main__':
    s=Solution()
    # print(s.twoSum([3,2,4],6))
    # print(s.twoSum([3,3],6))
    print(s.hammingDistance(93,73))
    # print(s.hammingDistance(1,4))
    # print(s.hammingDistance(4,2))
    # print(s.hammingDistance_fastest(93,73))
