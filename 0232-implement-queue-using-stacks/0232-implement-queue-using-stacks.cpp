#include <stack>

class MyQueue {
public:
    stack<int> stack1; 
    stack<int> stack2; 
    MyQueue() {

    }
    
    void push(int x) {
        stack1.push(x);
    }
    
    int pop() {
        while(!stack1.empty()){
            int val = stack1.top();
            stack2.push(val);
            stack1.pop();
        }
        int res = stack2.top();
        stack2.pop();
        while(!stack2.empty()){
            int val = stack2.top();
            stack1.push(val);
            stack2.pop();
        }
        return res;
    }
    
    int peek() {
        while(!stack1.empty()){
            int val = stack1.top();
            stack2.push(val);
            stack1.pop();
        }
        int res = stack2.top();
        while(!stack2.empty()){
            int val = stack2.top();
            stack1.push(val);
            stack2.pop();
        }
        return res;
    }
    
    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */