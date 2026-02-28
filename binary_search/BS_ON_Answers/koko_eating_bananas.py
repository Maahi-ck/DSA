class Solution:
    def minEatingSpeed(self, piles, h):
        low=1
        high =max(piles)
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            ## number of hours to required to eat all bananas if koko eats mid number of bananas per hour
            number_of_hours=self.calculateHours(piles, mid)
            if number_of_hours <= h:
                ## it is possible to eat all piles in h hours if koko eats at speed mid so store in result
                result = mid
                ## trying for less speed as koko wants to eat slow
                high = mid - 1
            else:
                ## taking more than h hours to eat all bananas ...... so lets try for more speed 
                low = mid + 1

        return result

    def calculateHours(self, piles, k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours