#include<iostream>
#include<string>
using namespace std;

int lengthOfLastWord(string s) {
    while(*(s.end()-1) == ' '){
        s = s.substr(0, s.length()-1);
    }
    s = " "+s;

    for(int i=s.length(); i>=0; i--){
        if(s[i]==' ')return s.length()-i-1;
    }
    return 0;
}

int main(){
    cout<<lengthOfLastWord("a   ")<<endl;
}
