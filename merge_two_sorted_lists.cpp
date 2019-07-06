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

int main(){
    ListNode* head = new ListNode(1);
    head->push_back(2);
    head->push_back(3);
    head->show();
    head->clear();
}
