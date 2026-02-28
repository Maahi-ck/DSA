#include<bits/stdc++.h>
using namespace std;

void union_(vector<int>&a,vector<int>&b){
       unordered_map<int,int>mpp;
       for(auto it:a){mpp[it]++;}
       for(auto it:b){mpp[it]++;}

       for(auto it:mpp){
            cout<<it.first<<" ";
       }
       cout<<endl;
}

void intersection(vector<int>&a,vector<int>&b){
       unordered_map<int,int>mpp;
       unordered_map<int,int>ans;
       for(auto it:a){mpp[it]++;}

       for(auto it:b){
              if(mpp.find(it)!=mpp.end()){
                   ans[it]++;
              }
       }

       for(auto it:ans){
            cout<<it.first<<" ";
       }
       cout<<endl;
}

int main(){
       int n,m;
       cin>>n>>m;

       vector<int>a(n),b(m);
       for(int i=0;i<n;i++){
              cin>>a[i];
       }
       for(int i=0;i<m;i++){
            cin>>b[i];
       }

       union_(a,b);
}