def min_dis_recursion(s1, s2):
    def dp(i, j):
        # 删除多余的字符
        if i == -1: return j + 1
        if j == -1: return i + 1

        # 当前字符相同，跳过
        if s1[i] == s2[j]:
            return dp(i - 1, j -1)
        else:
            return min(
                #插入
                dp(i, j - 1) + 1,
                #删除
                dp(i - 1, j) + 1,
                #替换
                dp(i - 1, j - 1) + 1,
            )

    return dp(len(s1) - 1, len(s2) - 1)

print(min_dis_recursion('love', 'lov'))