def fun(v, k):
    n = len(v)
    prefix = {0: -1}

    current_prefix_sum = 0
    ans = 0

    for i in range(n):
        current_prefix_sum += v[i]
        required = current_prefix_sum - k

        if required in prefix:
            ans = max(ans, i - prefix[required])

        # store first occurrence only (important!)
        if current_prefix_sum not in prefix:
            prefix[current_prefix_sum] = i

    return ans


n, k = map(int, input().split())
v = list(map(int, input().split()))

print(fun(v, k))
