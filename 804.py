class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transforms=set()
        for word in words:
            s=''
            for c in word:
                s+=trans[ord(c)-ord('a')]
            transforms.add(s)
        return len(transforms)


if __name__ == '__main__':
    s=Solution()
    # print(s.twoSum([3,2,4],6))
    # print(s.twoSum([3,3],6))
    print(s.uniqueMorseRepresentations( ["gin", "zen", "gig", "msg"] ))
