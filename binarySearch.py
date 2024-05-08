def binary_search(nums,item):

    left, right= 0, len(nums)

    while right > left:
        middle = (left + right) // 2
        if nums[middle] > item:
            right = middle
        elif nums[middle] < item :
            left = middle + 1
        else:
            return middle
    return -1

nums = [2, 3, 4, 10, 40]
item = 10
result = binary_search(nums, item)
if result != -1:
    print("Element is  at index", str(result))
else:
    print("Element is not  in the list")