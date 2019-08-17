#include<iostream>
#include<vector>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if(strs.size() == 0) return "";
    string LCP = strs[0];

    for(string word : strs)
        if(word.length() < LCP.length()) LCP = word;

    for(string word : strs){
        for(int i=0; i<LCP.length(); i++){
            if(word[i] != LCP[i]){
                LCP = LCP.substr(0, i);
                break;
            }
        }
    }
    return LCP;
}

int main(){
    vector<string> input{"flower", "flow", "flight"};
    cout<<longestCommonPrefix(input)<<endl;
}
