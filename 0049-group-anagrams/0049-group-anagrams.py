class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # Sorted strings are equal if anagrams
        result = {}
        for string in strs:
            sort_str = tuple(sorted(string))
            if sort_str not in result:
                result[sort_str] = [string]
            else: 
                result[sort_str].append(string)
        res = [v for k, v in result.items()]
        return res