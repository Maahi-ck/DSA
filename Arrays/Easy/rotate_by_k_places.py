def rotate_right(nums, k):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        ans[(i + k) % n] = nums[i]
        
    for i in range(n):
        nums[i] = ans[i]  # update in-place


def rotate_left(nums, k):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        ans[(i + n -k ) % n] = nums[i]

    for i in range(n):
        nums[i] = ans[i]  # update in-place
        

# Example usage
n, k = map(int, input().split())
v = list(map(int, input().split()))

rotate_left(v, k)
print("After left rotation:", v)

rotate_right(v, k)
print("After right rotation:", v)
