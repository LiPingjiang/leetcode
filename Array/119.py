class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            ret=[1]
            for i in range(1,rowIndex+1):
                ret=self.next_row(ret)
            return ret

    def next_row(self,row):
        ret=[1]
        l=len(row)
        for idx in range(0,l-1):
            # print(('idx',idx))
            cell = row[idx]+row[idx+1]
            ret.append(cell)
        ret.append(1)
        # ret.extend(1)
        return ret

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.getRow(3))
    print("Time Used: " + str(time.clock() - start))