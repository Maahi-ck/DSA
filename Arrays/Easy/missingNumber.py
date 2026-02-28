def missingNumber(nums):
    n = len(nums)
    ans=n*(n+1)/2
    for x in nums:
        ans = ans - x
    return ans
