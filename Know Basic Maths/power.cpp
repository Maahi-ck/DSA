#include<bits/stdc++.h>
using namespace std;

// brute force
// Time complexity = O(b)
long long power1(int a,int b){
       long long ans=1;
       for(int i=1;i<=b;i++){
             ans=ans*a;
       }
       return ans;
}

//optimised
// Time Complexity = O( log(b) )
long long power2(int a,int b){
        long long ans=1;
        while(b>0){
               if(b%2==1){ans=ans*a; b--;}
               a=a*a;
               b=b/2;
        }
        return ans;
}
int main(){
        int a=3,b=5;
        cout<<power1(a,b)<<endl;
        cout<<power2(a,b)<<endl;
}