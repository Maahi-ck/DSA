def binary_search(nums,target):
        n=len(nums)
        left=0
        right=n-1
        while left<=right :
                mid =(left+right)//2
                if nums[mid]==target :
                         return mid
                elif nums[mid]<target :
                        left=mid+1
                else :
                      right=mid-1
        return -1

## first element in array >= target
def lower_bound(nums,target):
        n=len(nums)
        ans=n
        left=0
        right=n-1
        while left<=right :
                mid =(left+right)//2
                if nums[mid]>=target :
                        ## condition satisfied hence stored in ans and search for more less on left side
                        ans=mid 
                        right=mid-1
                else :
                       left=mid+1
        return ans

## first element in array > target
def upper_bound(nums,target):
        n=len(nums)
        ans=n
        left=0
        right=n-1
        while left<=right :
                mid =(left+right)//2
                if nums[mid]>target :
                         ## condition satisfied hence stored in ans and search for more less on left side
                        ans=mid 
                        right=mid-1
                else :
                       left=mid+1
        return ans

## insert position of target in nums = lower_bound index
def search_insert_position(nums,target):
        return lower_bound(nums,target)


def first_and_last_occurance(nums,target):
        first_occurance=lower_bound(nums,target)
        last_occurance=upper_bound(nums,target)-1

def count_occurances(nums,target):
        first=lower_bound(nums,target)        
        last=upper_bound(nums,target)-1
        return last-first+1

def minimum_in_rotated_sorted(nums):
        n=len(nums)
        if n==1 :
                return 0
        
        ## not rotated
        if nums[0]<nums[n-1]:
                return 0
        
        left=0
        right=n-1
        while left<=right :
                mid=(left+right)//2
                if nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1] :
                        return mid
                ## sorted left part -> minimum wont be here
                elif nums[0]<nums[mid]:
                        left=mid+1
                else :
                        right=mid-1

## also known as peak element
## maximum value index = minimum value index - 1 for a rotated sorted array
def maximum_in_rotated_sorted(nums):
        n=len(nums)
        ## not rotated
        if nums[0]<nums[n-1]:
                return n-1

        return minimum_in_rotated_sorted(nums)-1

def number_of_times_rotated(nums):
        return minimum_in_rotated_sorted(nums) 

def search_in_rotated_sorted(nums,target):
        maxi=maximum_in_rotated_sorted(nums)
        n=len(nums)
        ans=binary_search(nums[0:maxi+1],target)
        if ans==-1:
                return binary_search(nums[maxi+1:n],target)
        else :
            return ans
                

