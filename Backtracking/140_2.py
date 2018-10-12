import operator
# 递归，使用hash表存储计算结果

class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]+suffix
        """
        res_hash = {}
        def run(s):
            # print(s)
            if s in res_hash:
                return res_hash[s]
            res = []
            if s in wordDict:
                res.append(s)
            for word in wordDict:
                if s.find(word) == 0:
                    sub_res=run(s[len(word):])
                    if len(sub_res) > 0 :
                        res.extend(map(lambda x: word + " " + x, sub_res))

            res_hash[s] = res
            return res
        return run(s)

if __name__ == '__main__':
    import time
    start = time.clock()
    s=Solution()
    # print(s.wordBreak( "catsanddog", ["cat","cats","and","sand","dog"] ))
    print(s.wordBreak( "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] ))
    # print(s.wordBreak( "aaaaaaaaaaaaadaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"] ))
    # print(s.wordBreak( "a", ["a"] ))
    print("Time Used: " + str(time.clock() - start))