class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add=True
        for i in range(len(digits)-1,-1,-1):
            # print(i)
            if add:
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    add=False
                    break
        if add:
            tmp_list = [1]
            tmp_list.extend(digits)
            return tmp_list
        return digits


if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.removeElement([]))
    # print(s.plusOne([4,3,2,1]))
    print(s.plusOne([9,9]))
    print("Time Used: " + str(time.clock() - start))