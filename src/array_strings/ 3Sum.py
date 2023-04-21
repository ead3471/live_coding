# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def test_1():
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
    assert [[-1, -1, 2], [-1, 0, 1]] == threeSum(nums)


def threeSum(nums: list):
    result = set()
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            if nums[i]+nums[j] > 0:
                break
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add({nums[i], nums[j], nums[k]})

    return result


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
