#include<bits/stdc++.h>
using namespace std;

bool linear_search(vector<int>&v,int ele){
          for(auto it:v){
                if(it==ele){return true;}
          }
          return false;
}

int main(){
       int n;
       cin>>n;

       vector<int>v(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       int ele;
       cin>>ele;

       cout<<linear_search(v,ele)<<endl;
}