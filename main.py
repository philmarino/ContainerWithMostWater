def maxArea(height):
    maxArea = 0
    length = len(height)
    for i in range(length - 1):
        for j in range(i+1, length):
            area = min(height[i], height[j]) * (j-i)
            if area > maxArea:
                maxArea = area

    return maxArea


# Example 1:
# Input:
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: 
height = [1,1]
print(maxArea(height))
# Output: 1
