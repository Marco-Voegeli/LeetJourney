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
        // Remove elements until we land on the same element again
        ListNode* p1 = head;
        ListNode* p2 = head;
        if (p1 == NULL){
            return false;
        }
        while(p1->next != NULL && p1->next->next != NULL){
            p1 = p1->next->next;
            p2 = p2->next;
            if(p1 == p2){
                return true;
            }
        }
        return false;
    }
};