# 四件事：
# #
# # 找出所有偶数 → 装进新列表
# # 找出所有大于 30的 → 装进新列表
# # 统计 20~50 之间（含 20 和 50）有几个
# # 从大到小排序输出
def get_evens(lst):
    """返回所有偶数"""
    result = []
    for n in lst:
        if n % 2 == 0:
            result.append(n)
    return result


def get_big(lst, threshold=30):
    """返回所有大于 threshold 的数，默认 30"""
    result = []
    for n in lst:
        if n > threshold:
            result.append(n)
    return result


def count_between(lst, low, high):
    """统计 low~high 之间的数量（含两端）"""
    count = 0
    for n in lst:
        if low <= n <= high:
            count += 1
    return count


def sort_desc(lst):
    """从大到小排序，返回新列表"""
    return sorted(lst, reverse=True)


# 主流程
nums = [12, 45, 8, 33, 21, 60, 17, 99, 5, 40]

print(get_evens(nums))
print(get_big(nums))
print(count_between(nums, 20, 50))
print(sort_desc(nums))