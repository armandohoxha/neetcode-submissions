class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            new_max_area = (right - left) * (min(heights[left], heights[right]))
            if new_max_area > max_area:
                max_area = new_max_area
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

        