def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return right
peak_index = findPeakElement([1,2,3,1])
print("The peak element is at index", peak_index, "with value", [1,2,3,1][peak_index])
