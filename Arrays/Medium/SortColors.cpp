#include<bits/stdc++.h>
using namespace std;

void SortColors(vector<int>&v){
         int a=0,b=0,c=0;
         for(auto it:v){
               if(it==0){a++;}
               else if(it==1){b++;}
               else if(it==2){c++;}
         }
         int idx=0;
         for(int i=0;i<a;i++){ v[idx]=0; idx++; }
         for(int i=0;i<b;i++){ v[idx]=1; idx++; }
         for(int i=0;i<c;i++){ v[idx]=2; idx++; }
}

int main(){
       int n;
       cin>>n;

       vector<int>v(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       SortColors(v);
}