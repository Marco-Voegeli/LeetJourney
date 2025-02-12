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
        while(p1 != NULL){
            p1 = p1->next;
            if(p1 == p2){
                return true;
            }
            if(p1 != NULL){
            p1 = p1->next;
            if (p1 == p2){
                return true;
            }
            p2 = p2->next;
            }
        }
        return false;
    }
};