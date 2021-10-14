def countSmaller(arr):
    res = [0] * len(arr)

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        # print(left, right)
        return merge(left, right)

    def merge(left, right):
        tmp = []
        i = 0
        j = 0
        while i < len(left) or j < len(right):
            if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                tmp.append(left[i])
                res[left[i][0]] += j
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        return tmp

    merge_sort(arr)
    return sum(res)

l = [363, 112, 133, 477, 375, 892, 804, 189, 33, 103, 569, 229, 591, 638, 630, 110, 3, 195, 423, 949]
r = countSmaller(l)
print(r)