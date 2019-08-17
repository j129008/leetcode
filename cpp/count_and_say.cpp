#include<iostream>
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

    vector<string> spliter(string x){
        vector<string> return_string;
        int head = 0, i = 0;
        for(i=0; i<x.length()-1; i++){
            if(x[i] != x[i+1]){
                return_string.push_back(x.substr(head, i+1-head));
                head = i+1;
            }
        }
        return_string.push_back(x.substr(head, x.length()-head));
        return return_string;
    }

    string talker(string x){
        string talk = "";
        for(string ele : spliter(x))
            talk += to_string(ele.length())+ele[0];
        return talk;
    }

    unordered_map<string, string> history;
    unordered_map<string, string>::iterator iter;
    string countAndSay(int n) {
        string start = "1";
        for(int i=1; i<n; i++){
            iter = history.find(to_string(i));
            if(iter != history.end()){
                start = iter->second;
            }else{
                start = talker(start);
                history[to_string(i)] = start;
            }
        }
        return start;
    }


int main(){
    cout<<countAndSay(5)<<endl;
}
