
class Solution {
public:
    string clearDigits(string s) {
        int p = 0;
        while (!isdigit(s[p])){
            if (p == s.length())
                return s;
            p += 1;
        }
        s.erase(p-1, 2);
        return clearDigits(s);

    }
};