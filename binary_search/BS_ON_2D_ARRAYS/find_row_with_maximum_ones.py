## first element in array >= target
def lower_bound(nums,target):
        n=len(nums)
        ans=-1
        left=0
        right=n-1
        while left<=right :
                mid =(left+right)//2
                if nums[mid]>=target :
                        ## condition satisfied hence stored in ans and search for more less on left side
                        ans=mid 
                        high=mid-1
                else :
                       low=mid+1
        return ans

def row_with_maximum_ones(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    ans=0
    maxones=0
    for row in range(0,rows) :
          first=lower_bound(matrix[row],1)
          last=cols-1
          number_of_ones=last-first+1
          
          if number_of_ones > maxones :
                 maxones=number_of_ones
                 ans=row
    return ans