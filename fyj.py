def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print("列表中所有元素的和为：", sum_of_list(numbers))
