## first element in array > target
def upper_bound(nums,target):
        n=len(nums)
        ans=-1
        left=0
        right=n-1
        while left<=right :
                mid =(left+right)//2
                if nums[mid]>target :
                         ## condition satisfied hence stored in ans and search for more less on left side
                        ans=mid 
                        high=mid-1
                else :
                       low=mid+1
        return ans


def find(matrix,target):
    ans=0
    for row in matrix:
           ans+=upper_bound(row,target)

def median(matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        total_elements= rows*cols

        left=0
        right=rows*cols-1

        while left <= right :
            mid=(left+right)//2
            curr_row=mid/cols
            curr_column=mid%cols
            
            count=find(matrix,mid)

            if  count == total_elements /2 :
                    return matrix[curr_row][curr_column]
            elif count < total_elements /2 :
                    low=mid+1
            else :
                    high=mid-1