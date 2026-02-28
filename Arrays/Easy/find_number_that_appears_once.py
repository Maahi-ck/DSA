def single_number(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans


n = int(input())
nums = list(map(int, input().split()))

print(single_number(nums))
