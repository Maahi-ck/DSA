 #include<bits/stdc++.h>
 using namespace std;

 void moveZeroes(vector<int>& nums) {
          int n=nums.size();
          int firstzero=0;
          for(int i=0;i<n;i++){
                 if(nums[i]!=0){
                      while(firstzero<n && nums[firstzero]!=0){firstzero++;}
                      if(firstzero<i){
                      swap(nums[firstzero],nums[i]);}
                 }
          }
    }

int main(){
       int n;
       cin>>n;
       vector<int>v(n);
       for(int i=0;i<n;i++){
           cin>>v[i];
       }

       moveZeroes(v);
}