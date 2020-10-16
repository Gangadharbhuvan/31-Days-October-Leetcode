'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104





'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        if r==0:return False
        c=len(matrix[0])
        lo=0
        hi=r*c -1
        while (lo<=hi):
            mid=(lo+hi)//2
            x=mid//c
            y=mid%c
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                hi=mid-1
            else:
                lo=mid+1
        return False