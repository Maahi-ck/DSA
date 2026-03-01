def sqrt(n):
    if n==0 or n==1:
        return n 
       
    low=1
    high=n-1
    while low<=high:
           mid=(low+high)//2
           square_value=mid*mid
           if square_value == n :
                return mid
           elif square_value > n :
                  high=mid-1
           else :
                low=mid+1

    return -1