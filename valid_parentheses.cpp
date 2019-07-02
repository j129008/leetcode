#include<iostream>
#include<string>
#include<stack>
#include<unordered_map>
using namespace std;


bool isValid(string s) {
    unordered_map<char, char> bracket = {
        {')', '('},
        {'}', '{'},
        {']', '['}
    };
    unordered_map<char, char>::iterator iter;
    stack<char> stack;

    for(char ch : s){
        iter = bracket.find(ch);
        if(iter != bracket.end()){
            if(!stack.empty()){
                if(bracket[ch] == stack.top()){
                    stack.pop();
                    continue;
                }
            }
        }
        stack.push(ch);
    }

    if(stack.size() == 0) return true;
    return false;
}


int main(){
    cout<<isValid("[[[]]][")<<endl;

}
