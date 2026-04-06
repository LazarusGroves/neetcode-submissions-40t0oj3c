class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Pass forward -> back
        forward_coefficient = 1;
        for i, num in enumerate(nums):
            result[i] = forward_coefficient;
            forward_coefficient *= num

        backward_coefficient = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= backward_coefficient;
            backward_coefficient *= nums[i]

        return result