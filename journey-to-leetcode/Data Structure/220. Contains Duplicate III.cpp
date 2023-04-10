#include<iostream>
#include<bits/stdc++.h>

using namespace std;
class Solution {
public:
    bool containsNearbyAlmostDuplicateNot(vector<int>& nums, int indexDiff, int valueDiff) {
//        unordered_map <int,int> arr;
//
//        for(int i =0; i< nums.size(); i++){
//            if(arr[nums[i]] != 0 ){
//                int diffInIndx = abs (i - arr[nums[i] +1);
//                int diffInVal = abs (nums[i] - valueDiff);
//                if(diffInIndx <= indexDiff && diffInVal <=valueDiff){
//                    return true;
//                }
//                else {
//                    arr[nums[i]] = i+1;
//                }
//            }
//            else {
//                arr[nums[i]] = i+1;
//            }
//        }
//            return false;
    }


    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {

        for (int i = 0; i < nums.size(); i++){
            for (int j =0; j < nums.size(); j++){
                if(i!=j && abs(i-j) <= indexDiff && abs(nums[i] - nums[j]) <= valueDiff){
                    return true;
                }
            }
        }
                    return false;
    }
};

int main()
{
    cout << "Hello World" << endl;

    Solution ob;
    vector<int> nums = {1,2,3,1,2,3 };
    vector<int> nums2 = {1,2,3,1};
    vector<int> nums3 = {1,5,9,1,5,9};

    bool output = ob.containsNearbyAlmostDuplicate(nums3, 2, 3);
    cout << "Output of checkers "<< output << endl;
}


