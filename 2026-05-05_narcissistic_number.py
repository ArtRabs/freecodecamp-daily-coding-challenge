def is_narcissistic(n):

    nums = list(map(int, str(n)))

    total = 0

    for num in nums:

        total += num ** len(nums)

    return total == n