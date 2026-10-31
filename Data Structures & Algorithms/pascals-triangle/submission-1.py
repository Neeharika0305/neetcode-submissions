from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list to store all rows
        triangle = []
        
        for i in range(numRows):
            # Create a new row initialized with 1s. 
            # The length of the row matches the 0-indexed row number + 1.
            row = [1] * (i + 1)
            
            # Fill the inner elements (excluding the first and last elements)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Append the completed row to the triangle
            triangle.append(row)
            
        return triangle
