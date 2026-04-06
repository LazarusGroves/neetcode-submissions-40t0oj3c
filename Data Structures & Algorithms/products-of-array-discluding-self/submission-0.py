class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = nums.copy()

        # Pass forward -> back
        forward_coefficient = 1;
        i = 0
        while i < len(nums):
            result[i] = forward_coefficient;
            forward_coefficient *= nums[i]
            i+=1

        backward_coefficient = 1
        i = len(nums) - 1
        while i >= 0:
            result[i] *= backward_coefficient;
            backward_coefficient *= nums[i]
            i-=1

        return result