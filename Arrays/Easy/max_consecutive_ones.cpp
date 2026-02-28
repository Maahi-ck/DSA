 #include<bits/stdc++.h>
 using namespace std;

 int findMaxConsecutiveOnes(vector<int>& nums) {
           int ans=0;
           int current_count=0;
           int n=nums.size();
           for(int i=0;i<n;i++){
                  if(nums[i]==1){
                         current_count++;
                         ans=max(ans,current_count);
                  }else{
                      current_count=0;
                  }
           }
           return ans;
    }


int main(){
         int n; cin>>n;
         vector<int>v(n);

         for(int i=0;i<n;i++){
               cin>>v[i];
         }

         cout<<findMaxConsecutiveOnes(v)<<endl;
}