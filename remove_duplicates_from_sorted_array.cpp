#include<iostream>
#include<vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if(nums.size() <= 1) return nums.size();
    int length = nums.size()-1;
    int i = 0;
    while(i != length){
        if(nums[i] == nums[i+1]){
            nums.erase(nums.begin()+i);
            length--;
        }else{
            i++;
        }
    }
    return nums.size();
}

int main(){
    vector<int> nums{1, 1, 1, 1, 1, 2, 3, 4, 4, 4};
    removeDuplicates(nums);
    for(int i=0; i<nums.size(); i++){
        cout<<nums[i]<<endl;
    }
}
