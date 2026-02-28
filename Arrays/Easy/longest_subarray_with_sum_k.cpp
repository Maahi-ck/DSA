#include<bits/stdc++.h>
using namespace std;

int fun(vector<int>&v,int k){
       int n=v.size(); 
       unordered_map<int,int>prefix;
        prefix[0]=-1;

        int current_prefix_sum=0;
        int ans=0;
        for(int i=0;i<n;i++){
               current_prefix_sum+=v[i];
               int required=current_prefix_sum-k;
               if(prefix.find(required)!=prefix.end()){
                        ans=max(ans,i-prefix[required]);
               }
        }
        return ans;
}

int main(){
       int n,k;
       cin>>n>>k;

       vector<int>v(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       cout<<fun(v,k)<<endl;
}