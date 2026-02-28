#include<bits/stdc++.h>
using namespace std;

int largest(vector<int>&v){
       int maxi=INT_MIN;
       for(auto it:v){
               maxi=max(maxi,it);
       }
       return maxi;
}

int main(){
       vector<int>v;
       int n;
       cin>>n;

       v=vector<int>(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       cout<<largest(v)<<endl;
}