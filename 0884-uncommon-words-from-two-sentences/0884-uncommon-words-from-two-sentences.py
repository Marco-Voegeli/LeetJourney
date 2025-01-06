class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        all_words_dups = (s1 + " " + s2).split()
        res = []
        duplicates = []
        for word in all_words_dups:
            if word not in duplicates:
                if word in res:
                    res.remove(word)
                    duplicates.append(word)
                else:
                    res.append(word)
        return res
        
            
        return res

        