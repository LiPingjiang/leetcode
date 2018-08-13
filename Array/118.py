class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            ret=[[1]]
            for i in range(1,numRows):
                ret.append(self.next_row(ret[i-1]))
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

    def generate_fastest(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        outputList = []

        for indexRow in range(0,numRows):
            rowList = [1] * int(indexRow+1)
            print(rowList)

            if len(rowList) > 2:
                previousRow = outputList[indexRow-1]
                # print(len(previousRow), indexRow)
                for indexPrev in range(1,indexRow):
                    rowList[indexPrev] = previousRow[indexPrev] + previousRow[indexPrev-1]
                    #  print('rowList:', indexRow, rowList, previousRow, len(rowList))
                    # print('outputList:', outputList)
            outputList.append(rowList)


        return outputList

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.generate(5))
    print("Time Used: " + str(time.clock() - start))