#include<bits/stdc++.h>
using namespace std;

void rotate_right(vector<int> &nums, int k)
{
      int n = nums.size();
      vector<int> ans(n);
      for (int i = 0; i < n; i++)
      {
            ans[(i + k) % n] = nums[i];
      }

      nums = ans;
}

void rotate_left(vector<int> &nums, int k)
{
      int n = nums.size();
      vector<int> ans(n);
      for (int i = 0; i < n; i++)
      {
            ans[(i - k + n) % n] = nums[i];
      }

      nums = ans;
}

int main()
{
      vector<int> v;
      int n,k;
      cin >> n>>k;

      v = vector<int>(n);
      for (int i = 0; i < n; i++)
      {
            cin >> v[i];
      }

      rotate_left(v,k);
      rotate_right(v,k);
}