class Solution:
    def find(bloomDay,k, day):
            number_of_boquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= day:
                    flowers += 1
                    if flowers == k:
                         number_of_boquets += 1
                         flowers = 0
                else:
                    flowers = 0
            return number_of_boquets
    
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        ## total number of flowers required to make m boquets = m * k
        ## available number of flowers = n
        if m * k > n:
            return -1
        
        ans=-1
        low = 1
        high = max(bloomDay)
        while low < high:
            mid = (low + high) // 2
            ## number_of_boquets we can make after mid days
            number_of_boquets=self.find(bloomDay,k,mid)

            if number_of_boquets >= m :
                 ## after mid days , we can make >=m boquets so mid is possible answer so store in ans
                 ans=mid
                 ## try for lesser number of days 
                 high=mid-1
            else:
                low = mid + 1
        
        return ans
        