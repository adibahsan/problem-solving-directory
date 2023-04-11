#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        int i =1;
        int j =1;
        for (; i<len;i++){
            if(nums[i] != nums[j-1]){
                nums[j] = nums[i];
                j++;
            }
        }

        return j;
    }
};

int main()
{
    cout << "26. Remove Duplicates from Sorted Array" <<endl;
    Solution solution;
    vector<int> input = {0,0,1,1,1,2,2,3,3,4};

    cout << "Tournament Winners" << endl << solution.removeDuplicates(input) <<endl;



}
