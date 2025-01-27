#include <stack>

class Solution {
    private:
            bool endBracket(char bracketType, stack<char> &brackets){
            if (brackets.empty()){
                return false;
            }
            if (brackets.top() == bracketType){
                brackets.pop();
                return true;
            }
                return false;
        }
public:
    bool isValid(string s) {
        stack<char> brackets;
        for(int i = 0; i < s.length(); i++){
          bool endBrackBool = true;
            switch (s[i]){
                case '(': 
                    brackets.push(s[i]);
                    break;
                case '{': 
                    brackets.push(s[i]);
                    break;
                case '[': 
                    brackets.push(s[i]);
                    break;
                case ')':
                    endBrackBool = endBracket('(', brackets);
                    break;
                case ']':
                    endBrackBool = endBracket('[', brackets);
                    break;
                case '}':
                    endBrackBool = endBracket('{', brackets);
                    break;
            };
            if(!endBrackBool){
                return endBrackBool;
            }

        }
        if (brackets.empty()){
            return true;
        }
        return false;
        };
};