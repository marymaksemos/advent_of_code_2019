def intcode(nums):
    idx = 0
    while nums[idx] != 99:
        num = nums[idx]
        val1 = nums[nums[idx + 1]]
        val2 = nums[nums[idx + 2]]
        idx3 = nums[idx + 3]
        if num == 1:
            nums[idx3] = val1 + val2
        elif num == 2:
            nums[idx3] = val1 * val2
        idx += 4
    return nums