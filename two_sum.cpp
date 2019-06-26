#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
    public:
        // Bruce Force
        vector<int> twoSumBF(vector<int>& nums, int target) {
            for(int i=0; i<nums.size(); i++)
                for(int j=i+1; j<nums.size(); j++)
                    if( (nums[i]+nums[j]) == target )
                        return vector<int> {i, j};
            return vector<int>{0, 0};
        }

        // Map
        vector<int> twoSumMap(vector<int>& nums, int target) {
            map<int, int> num_map;
            map<int, int>::iterator iter;
            for(int i=0; i<nums.size(); i++){
                iter = num_map.find(target - nums[i]);
                if(iter != num_map.end())
                    return vector<int>{i, iter->second};
                num_map[nums[i]] = i;
            }
            return vector<int>{0, 0};
        }
};

int main(){
    Solution sol = Solution();
    vector<int> input{3, 3};

    vector<int> ret = sol.twoSumBF(input, 6);
    cout<<ret[0]<<", "<<ret[1]<<endl;

    ret = sol.twoSumMap(input, 6);
    cout<<ret[0]<<", "<<ret[1]<<endl;

    return 0;
}
