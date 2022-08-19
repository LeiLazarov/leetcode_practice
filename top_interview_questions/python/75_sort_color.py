class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, i, blue = 0, 0, len(nums)-1
        
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                i += 1
                red += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1