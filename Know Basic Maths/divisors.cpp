#include<bits/stdc++.h>
using namespace std;

void print_divisors(int num){
       vector<int>div;
         for(int i=1;i*i<=num;i++){
               if(num%i==0){
                     div.push_back(i);
                     if(i*i !=num){
                          div.push_back(num/i);
                     }
               }
         }
         for(auto it:div){
              cout<<it<<" ";
         }
         cout<<endl;
}

int main(){
       int num;
       cout<<"Enter a number "<<endl;
       cin>>num;
       print_divisors(num);
}