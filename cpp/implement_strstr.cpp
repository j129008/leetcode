#include<iostream>
#include<string>
using namespace std;

int strStr(string haystack, string needle) {
    if(needle == "") return 0;
    if(haystack.find(needle) != string::npos)
        for(int i=0; i<haystack.length(); i++)
            for(int j=0; j<needle.length(); j++){
                if(haystack[i+j] != needle[j]){
                    j -= 1;
                    break;
                }
                if(j == needle.length()-1) return i;
            }
    return -1;
}

int main(){
    cout<<(strStr("mississippi", "issip"))<<endl;
}
