class Solution {
public:
    bool isPalindrome(string s) {
        int p1 = 0;
        int p2 = s.length() - 1;
        while(p1 < p2){
            char c1 = s[p1];
            char c2 = s[p2];
            if (c1 == ' '|| !isalnum(c1)) {
                p1 += 1;
                continue;
            }
            if (c2 == ' ' || !isalnum(c2)){
                p2 -= 1;
                continue;
            }
            if (tolower(c1) != tolower(c2)){
                return false;
            }
            p1 += 1;
            p2 -= 1;
        }
        return true;
    }
};