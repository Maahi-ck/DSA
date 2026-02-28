#include<bits/stdc++.h>
using namespace std;

bool check1(string &s){
     int n=s.size();
     string rev(n,' ');
     for(int i=0;i<n;i++){
           rev[i]=s[n-i-1];
     }

     for(int i=0;i<n;i++){
           if(s[i]!=rev[i]){return false;}
     }
     return true;
}

bool check2(string &s){
      int n=s.size();
      for(int i=0;i<n;i++){
            if(s[i]!=s[n-i-1]){return false;}
      }
      return true;
}

int main(){
       string s;
       cout<<"Enter a string "<<endl;
       cin>>s;
       cout<<check1(s)<<endl;
       cout<<check2(s)<<endl;

       // Time complexity :- O(length of string) = O(n)
}