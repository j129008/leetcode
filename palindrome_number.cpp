#include<iostream>
#include<string>
#include <limits.h>
using namespace std;

string reverse(int x){
    string str_x = to_string(x);
    string rev_x, ch;
    for( int i=str_x.size()-1; i>=0; i-- ){
        ch = str_x[i];
        rev_x += ch;
    }
    return rev_x;
}

bool isPalindrome(int x) {
    if(to_string(x) == reverse(x)) return true;
    return false;
}

int main(){
    cout<<isPalindrome(12321)<<endl;
}
