#include<iostream>
#include<string>
#include <limits.h>
using namespace std;

int postive_reverse(int x){
    string str_x = to_string(x);
    string rev_x, ch;
    for( int i=str_x.size()-1; i>=0; i-- ){
        ch = str_x[i];
        rev_x += ch;
    }
    long res = stol(rev_x);
    if (res > INT_MAX) return 0;
    return res;
}

int reverse(int x) {
    if(x == INT_MIN) return 0;
    if(x>=0) return postive_reverse(x);
    else return -postive_reverse(-x);
}

int main(){
    cout<<reverse(-2147483648)<<endl;
}
