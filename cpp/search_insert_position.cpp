#include<iostream>
#include<vector>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
    int i=0;
    for(i=0; i<nums.size(); i++)
        if(nums[i] >= target)
            return i;
    return i;
}

int main(){
    vector<int> nums{1, 3, 5, 6};
    cout<<searchInsert(nums, 7)<<endl;
}
