def moveZeroes(nums):
    n = len(nums)
    firstzero = 0

    for i in range(n):
        if nums[i] != 0:
            while firstzero < n and nums[firstzero] != 0:
                firstzero += 1
            if firstzero < i:
                nums[firstzero], nums[i] = nums[i], nums[firstzero]


n = int(input())
v = list(map(int, input().split()))

moveZeroes(v)
print(v)
