class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {num: i for i, num in enumerate(numbers)}
        for num in num_dict:
            difference = target - num
            if difference in num_dict and num_dict[num] < num_dict[difference]:
                return [num_dict[num] + 1, num_dict[difference] + 1]