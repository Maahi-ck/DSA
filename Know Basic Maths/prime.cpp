#include<bits/stdc++.h>
using namespace std;

// Time complexity = O( sqrt(num) )
bool check(int num){
         for(int i=2;i*i<=num;i++){
              if(num%i==0){return false;}
         }
         return true;
}

int main(){
       int num;
       cout<<"Enter a number "<<endl;
       cin>>num;
       cout<<check(num)<<endl;
}