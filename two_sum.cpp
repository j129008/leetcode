#include<iostream>
#include<vector>
using namespace std;

class Solution {
    public:
        // Bruce Force
        vector<int> twoSumBF(vector<int>& nums, int target) {
            for(int i=0; i<nums.size(); i++)
                for(int j=i; j<nums.size(); j++)
                    if( (nums[i]+nums[j]) == target )
                        return vector<int> {i, j};
            return vector<int>{0, 0};
        }
};

int main(){
    Solution sol = Solution();
    vector<int> input{2, 7, 11, 15};

    vector<int> ret = sol.twoSumBF(input, 17);
    cout<<ret[0]<<", "<<ret[1]<<endl;

    return 0;
}
