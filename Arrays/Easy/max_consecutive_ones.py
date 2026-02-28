def findMaxConsecutiveOnes(nums):
    ans = 0
    current_count = 0

    for x in nums:
        if x == 1:
            current_count += 1
            ans = max(ans, current_count)
        else:
            current_count = 0

    return ans


n = int(input())
nums = list(map(int, input().split()))

print(findMaxConsecutiveOnes(nums))
