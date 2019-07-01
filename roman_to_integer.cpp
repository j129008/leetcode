#include<iostream>
#include<string>
#include<unordered_map>
using namespace std;

unordered_map<string, int> roman_one_char = {
    {"I", 1},
    {"V", 5},
    {"X", 10},
    {"L", 50},
    {"C", 100},
    {"D", 500},
    {"M", 1000}
};

unordered_map<string, int> roman_two_char = {
    {"IV", 4},
    {"IX", 9},
    {"XL", 40},
    {"XC", 90},
    {"CD", 400},
    {"CM", 900}
};

int romanToInt(string s) {
    int roman_int = 0;
    unordered_map<string, int>::iterator iter;
    while(s.size() != 0){
        string head = s.substr(0,2);
        iter = roman_two_char.find(head);
        if(iter != roman_two_char.end()){
            s.erase(0, 2);
            roman_int += iter->second;
        }else{
            head = s.substr(0,1);
            s.erase(0, 1);
            iter = roman_one_char.find(head);
            roman_int += iter->second;
        }
    }

    return roman_int;
}

int main(){
    cout<<romanToInt("IVVVVV")<<endl;
}
