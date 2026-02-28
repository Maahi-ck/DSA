#include<bits/stdc++.h>
using namespace std;

// Time complexity = O( number of digits ) = O( log(num) )
// a Number num contains log(num) digits

int count_digits(int num){
       int ans=0;
       while(num!=0){
              num=num/10;
              ans++;
       }
       return ans;
}

int main(){
       int num;
       cout<<"Enter a number "<<endl;
       cin>>num;
       cout<<count_digits(num)<<endl;
}