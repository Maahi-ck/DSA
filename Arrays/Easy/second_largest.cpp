#include<bits/stdc++.h>
using namespace std;

int Second_largest(vector<int>&v){
       int maxi1=INT_MIN,maxi2=INT_MIN;
       for(auto it:v){
               if(it>maxi1){
                    maxi2=maxi1;
                    maxi1=it;  
               }else if(it>maxi2){
                      maxi2=it;
               }
       }
       return maxi2;
}

int main(){
       vector<int>v;
       int n;
       cin>>n;

       v=vector<int>(n);
       for(int i=0;i<n;i++){
              cin>>v[i];
       }

       cout<<Second_largest(v)<<endl;
}