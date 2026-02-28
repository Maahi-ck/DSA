#include<bits/stdc++.h>
using namespace std;

bool check(vector<int>&v){
        int n=v.size();
        for(int i=1;i<n;i++){
               if(v[i]<v[i-1]){return false;}
        }
        return true;
}

int main(){
       vector<int>v;
       int n;
       cin>>n;

       v=vector<int>(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       cout<<check(v)<<endl;
}