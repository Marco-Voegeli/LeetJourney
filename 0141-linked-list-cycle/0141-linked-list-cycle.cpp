/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        int counter = 0;
        ListNode* curr = head;
        while(curr != NULL){
            if (counter > 10000)
                return true;
            curr = curr->next;
            counter += 1;
        }
        return false;
    }
};