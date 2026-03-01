def Nthroot(num,n):
    if num==0 or num ==1 :
        return num
       
    low=1
    high=n-1
    while low<=high:
           mid=(low+high)//2
           mid_power_n=pow(mid,n)
           if mid_power_n == num :
                return mid
           elif mid_power_n > num :
                  high=mid-1
           else :
                low=mid+1
    return -1

