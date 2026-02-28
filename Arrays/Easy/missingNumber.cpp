#include <bits/stdc++.h>
using namespace std;

int missingNumber(vector<int> &nums)
{
       int n = nums.size();
       vector<int> freq(n + 1, 0);
       for (int i = 0; i < n; i++)
       {
              freq[nums[i]]++;
       }
       for (int i = 0; i <= n; i++)
       {
              if (freq[i] == 0)
              {
                     return i;
              }
       }
       return -1;
}

int main()
{
       int n;
       cin >> n;

       vector<int> v(n);
       for (int i = 0; i < n; i++)
       {
              cin >> v[i];
       }

       cout << missingNumber(v) << endl;
}