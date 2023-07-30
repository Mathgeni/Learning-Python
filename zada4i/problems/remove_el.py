def removeElement(nums: list[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            j = i + 1
            while j < len(nums) and j == val:
                j += 1
            nums = nums[:i] + nums[i:j]
        else:
            i += 1
    return nums


if __name__ == '__main__':
    print(removeElement([3, 2, 2, 3], 3))
