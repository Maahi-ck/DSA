#include<bits/stdc++.h>
using namespace std;

int  reverse_number(int num){
       int ans=0;
       while(num!=0){
              int r=num%10;
              ans=(ans*10 + r);
              num=num/10;
       }
       return ans;
}

int main(){
       int num;
       cout<<"Enter a number "<<endl;
       cin>>num;
       cout<<reverse_number(num)<<endl;
}