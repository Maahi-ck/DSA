class Solution:
    def find(capacity,weights):
            days = 1
            current_load = 0
            for i in weights:
                if current_load + i > capacity:
                    days += 1
                    current_load = i
                else:
                    current_load += i
            return days
    
    def shipWithinDays(self, weights, days):
        sum=0
        for i in weights:
            sum+= i

        low = max(weights)
        high=sum
        ans=-1
        while low <= high :
            mid = (low + high) // 2
            number_of_days=self.find(mid,weights)
            if number_of_days <= days:
                 ans=mid
                 high=mid-1
            else:
                low = mid + 1

        return low