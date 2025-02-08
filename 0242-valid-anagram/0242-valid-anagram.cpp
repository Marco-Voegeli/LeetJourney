#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }
        unordered_map<char, int> wordCount2;
        unordered_map<char, int> wordCount1;
        for(int i = 0; i < s.length(); i++){
            wordCount2[s[i]] += 1;
            wordCount1[t[i]] += 1;
        }
        return wordCount2 == wordCount1;
    }
};