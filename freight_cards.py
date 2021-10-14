def dp_helper(n, key, value, arr):
    if type(key) == int:
        if n == key:
            arr.append([key, 1])
    elif value > 0:
        m1, m2 = key
        add_value = value + 1
        if n < m1:
            arr.append([(n, m2), add_value])
        elif n < m2:
            arr.append([(m1, n), add_value])

def dp(nums):
    max_v = max(nums)
    min_v = min(nums)
    memo = {}

    for m1 in range(min_v, max_v + 1):
        memo[m1] = 0
        for m2 in range(m1 + 1, max_v + 1):
            memo[m1, m2] = 0

    for n in nums:
        modify_arr = []

        for key, value in memo.items():
            t = []
            if type(key) == int:
                if value == 0 and n == key:
                    t = [key, 1]
                elif value == 1:
                    if n > key and memo[(key, n)] == 0:
                        t = [(key, n), 2]
                    elif n < key and memo[(n, key)] == 0:
                        t = [(n, key), 2]
            elif value > 0:
                m1, m2 = key
                add_value = value + 1
                if n < m1:
                    t = [(n, m2), add_value]
                elif n > m2:
                    t = [(m1, n), add_value]

            if t:
                modify_arr.append(t)

        modify_arr.sort(key=lambda x:x[1])
        for key, value in modify_arr:
            memo[key] = value
    return max([v for _,v in memo.items()])

# def dp(nums):
#     piles = [[nums[0]]]
#     for i in range(1, len(nums)):
#         piles_len = len(piles)
#
#         num = nums[i]
#         flag = False
#         for i in range(piles_len):
#             m = min(piles[i])
#             if num < m:
#                 piles[i].append(num)
#                 flag = True
#                 break
#
#         if not flag:
#             piles.append([num])
#
#     # print(piles)
#     # print(piles[1][0])
#     max_len = len(piles)



arr = '64 3 38 6 39 7 73 9 41 14 48 81 17 19 52 55 26 28 61 94'
arr = '57 47 50 4 26 1 60 44 30 54 19 21 52 32 24 15 45 8 16 22 55 46 12 39 36 25 9 28 11 7 23 51 35 40 29 37 58 53 34 18'
arr = [int(i) for i in arr.split()]
# arr = [5, 9, 1, 6, 8, 7, 3, 10, 4, 2]
# arr = [4, 5, 1, 3, 2]
# arr = [4, 5, 6, 1, 3, 8, 2, 7]
print(dp(arr))