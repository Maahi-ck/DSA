#include<bits/stdc++.h>
using namespace std;

vector<int> fun(vector<int>&v){
        int n=v.size();
        vector<int>ans;
        ans.push_back(v[0]);
        for(int i=1;i<n;i++){
             if(v[i]!=v[i-1]){
              ans.push_back(v[i]);
             }
        }
        return ans;
}

int main(){
       vector<int>v;
       int n;
       cin>>n;

       v=vector<int>(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       fun(v);
}