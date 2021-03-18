#include <iostream>
#include <vector>
#include<unordered_set>
using namespace std;


bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> int_set;
    for(unsigned int i=0;i<nums.size();i++){
        int_set.insert(nums[i]);
    }
    if(int_set.size() == nums.size()) return false;

    return true;
}


int main(){
    vector<int> nums{1, 2, 3, 1};
    cout<<containsDuplicate(nums)<<endl;
}
