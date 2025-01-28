/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head;
        ListNode* currNode;
        if (list2 == NULL){
            return list1;
        }
        if (list1 == NULL){
            return list2;
        }
        if (list1->val <= list2->val){
            head = list1;
            list1 = list1->next;

        } else{
            head = list2; 
            list2 = list2->next;
        }
        currNode = head;
        while(list1 != nullptr || list2 != nullptr){
            if (list2 == nullptr){
                currNode->next = list1;
                break;
            }            
            if (list1 == nullptr){
                currNode->next = list2;
                break;
            }
            if (list1->val <= list2->val){
                cout << list1->val;
                currNode->next = list1;
                list1 = list1->next;
            }
            else if (list1->val > list2->val){
                cout << list2->val;
                currNode->next = list2;
                list2 = list2->next;
            }
            currNode = currNode->next;
        }
        return head;
    }
};