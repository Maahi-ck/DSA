#include<bits/stdc++.h>
using namespace std;

// Time complexity :- O(log(min(a,b)))
int gcd(int a,int b){
      if(a==0){return b;}
      if(b==0){return a;}
      if(b>a){swap(a,b);}
      return gcd(b,a%b);
}

int main(){
         int a=42,b=48;
         cout<<gcd(a,b)<<endl;
}