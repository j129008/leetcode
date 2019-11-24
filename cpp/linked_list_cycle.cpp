#include<unordered_set>
#include<iostream>
using namespace std;

class ListNode{
    public:
        int val;
        ListNode *next;
        ListNode(int x): val(x), next(NULL) {}
};

class solution{
    public:
        bool hasCycle(ListNode *head){
            unordered_set<ListNode*> node_set;
            while(head != NULL){
                node_set.insert(head);
                head = head->next;
                unordered_set<ListNode*>::const_iterator got = node_set.find(head);
                if(got != node_set.end()) return true;
            }
            return false;
        }
};
