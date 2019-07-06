#include<iostream>
using namespace std;

class ListNode{
    public:
        ListNode(int);
        ListNode* tail();
        void push_back(int);
        void show();
        void clear();
        int val;
        ListNode* next;
};

ListNode::ListNode(int x){
    val = x;
    next = NULL;
}

ListNode* ListNode::tail(){
    ListNode* tail = this;
    while(tail->next != NULL)
        tail = tail->next;
    return tail;
}

void ListNode::push_back(int x){
    ListNode* tail = this->tail();
    tail->next = new ListNode(x);
}

void ListNode::show(){
    ListNode* node = this;
    while(node != NULL){
        cout<<node->val<<endl;
        node = node->next;
    }
}

void ListNode::clear(){
    ListNode* head = this;
    while(head != NULL){
        ListNode* select = head;
        head = select->next;
        delete select;
    }
}

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){
    ListNode ans = ListNode(-1);
    ListNode* tail = &ans;
    while((l1 != NULL) && (l2 != NULL)){
        if(l1->val > l2->val ){
            tail->next = l2;
            l2 = l2->next;
        }else{
            tail->next = l1;
            l1 = l1->next;
        }
        tail = tail->next;
    }
    if(l1 != NULL) tail->next = l1;
    else tail->next = l2;

    return ans.next;
}

int main(){
    ListNode* l1 = new ListNode(1);
    l1->push_back(2);
    l1->push_back(4);

    ListNode* l2 = new ListNode(3);
    l2->push_back(6);
    l2->push_back(7);

    ListNode* l3 = mergeTwoLists(l2, l1);
    l3->show();
    l3->clear();

    return 0;
}
