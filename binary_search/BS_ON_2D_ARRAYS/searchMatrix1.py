def searchMatrix(self,matrix,target):
    rows=len(matrix)
    cols=len(matrix[0])

    left=0
    right=rows*cols-1

    while left <= right :
           mid=(left+right)//2
           curr_row=mid/cols
           curr_column=mid%cols

           if matrix[curr_row][curr_column] == target :
                 return True
           elif matrix[curr_row][curr_column] < target :
                   low=mid+1
           else :
                 high=mid-1
    return False