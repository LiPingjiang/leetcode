#原始方法，tle

class Solution:

    def calculateNext(self, wordDict, prefix, suffix, pipeline, res):
        finish = True
        for word in wordDict:
            # print((suffix,word,suffix.find(word)))
            if suffix.find(word)==0:
                # print((suffix,word, suffix == word ))
                if suffix == word:
                    res.append((prefix+" "+suffix).strip())
                else:
                    pipeline.append((prefix+" "+word, suffix[len(word):]))
        return finish

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]+suffix
        """
        res=[]
        pipeline = [('',s)]
        finish = False
        while( not finish ):
            finish = True
            for element in pipeline:
                # print((element[0], element[1]))
                if not self.calculateNext( wordDict, element[0], element[1],pipeline, res):
                    finish = False

        return res


if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    print(s.wordBreak( "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["aa", "aaa", "aaaa", "aaaaa"]))
    # print(s.wordBreak( "catsanddog", ["cat","cats","and","sand","dog"] ))
    # print(s.wordBreak( "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] ))
    print("Time Used: " + str(time.clock() - start))