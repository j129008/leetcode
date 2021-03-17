#include <vector>
#include <iostream>
using namespace std;

class ListNode{
    public:
        int val;
        ListNode *next;
        ListNode(int x): val(x), next(NULL) {}
};


ListNode* reverseList(ListNode* head){
    if(head == NULL) return NULL;

    vector<ListNode*> ptrs;
    ListNode* it = head;
    while(it){
        ptrs.push_back(it);
        it = it->next;
    }

    for(unsigned int i=1;i<ptrs.size(); i++){
        ptrs[i]->next = ptrs[i-1];
    }

    ptrs[0]->next = NULL;

    return ptrs.back();
}


int main(){
    ListNode node1 = ListNode(1);
    ListNode node2 = ListNode(2);
    node1.next = &node2;
    ListNode* head = &node1;

    head = reverseList(head);
}
