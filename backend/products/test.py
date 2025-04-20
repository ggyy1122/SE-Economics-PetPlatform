def fun(arr: list):
    if not arr:  # 处理空列表的情况
        return None

    arr.sort()  # 先排序
    n = len(arr)
    current_count = 1  # 当前元素的连续出现次数
    max_count = 1  # 最高出现次数
    mode = arr[0]  # 众数初始化为第一个元素

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = arr[i - 1]
            current_count = 1  # 重置计数器

    # 检查最后一组连续元素
    if current_count > max_count:
        mode = arr[-1]

    return mode


arr={1,2,3,4,3,5,5,5,33,3,3}
print(fun(arr))