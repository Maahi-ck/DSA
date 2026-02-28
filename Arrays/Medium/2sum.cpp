#include <bits/stdc++.h>
using namespace std;

//using map 
// Time Complexity O(n)
// Space Complexity O(n)
vector<int> twoSum(vector<int> &nums, int target)
{

    int n = nums.size();
    unordered_map<int, int> mpp;

    for (int i = 0; i < n; i++)
    {
        int it = nums[i];
        if (mpp.find(target - it) != mpp.end())
        {
            return {mpp[target - it], i};
        }
        mpp[it] = i;
    }
    return {-1, -1};
}

// Using Sorting + Two Pointer
bool check(vector<int>&nums,int target){
         sort(nums.begin(),nums.end());
         int n=nums.size();

         int l=0,r=n-1;
         while(l<r){
               if(nums[l]+nums[r]==target){return true;}
               if(nums[l]+nums[r]>target){r--;}
               else{l++;}
         }
         return false;
}

int main()
{
    int n,target;
    cin >> n>>target;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    vector<int>ans=twoSum(v,target);
    cout<<ans[0]<<" "<<ans[1]<<endl;
}