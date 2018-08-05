class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A.find(B) > -1:
            return 1
        if (A+A).find(B) != -1: return 2
        la=len(A)
        lb=len(B)
        if la > lb :
            if (A+A).find(B) == -1:
                return -1
            else:
                return 2
        first=B.find(A)
        print(first)
        last=B[::-1].find(A[::-1])
        print(last)

        print(B[-last:])
        print( "A.find(B[-last:])   "+str(A.find(B[-last:])) )
        print( "A.find(B[0:first])  " + str(A.find(B[0:first])) )
        if last!=0 and (first == -1 or A.find(B[-last:]) != 0 or (first!=0 and A.find(B[0:first]) == -1)) : return -1
        start=first
        while( (start+la)<(lb-last) ):
            if B[start:start+la].find(A) == -1:
                return -1
            start+=la
        import math
        count=math.ceil((lb-first-last)/la) + math.ceil(first/la) + math.ceil(last/la)


        print("get count")
        # print(B[lb-la-la:lb])
        # print(math.ceil(first/la))
        # print(lb-la-1)
        return count


if __name__ == '__main__':
    s=Solution()
    # print(s.twoSum([3,2,4],6))
    # print(s.twoSum([3,3],6))
    # print(s.repeatedStringMatch("abcd" , "cdabcdab"))
    # print(s.repeatedStringMatch("aabaaabaaac","aabaaac"))
    # print(s.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab","ba"))
    # print(s.repeatedStringMatch("abaabaa"," abaababaab"))
    # print(s.repeatedStringMatch("abcd","abcdb"))
    # print(s.repeatedStringMatch("a","aa"))
    # print(s.repeatedStringMatch("abcd","cdabcdacdabcda"))
    # print(s.repeatedStringMatch("abcd", "cdabcdab"))
    print(s.repeatedStringMatch("abcd","bcdab"))
