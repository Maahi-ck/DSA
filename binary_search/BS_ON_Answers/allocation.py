class Solution:
    def noofstudents(self, n, arr, pages):
        count = 1        # Start with one student
        currpages = 0    # Current pages allocated to that student
        
        for i in range(n):
            if currpages + arr[i] <= pages:
                currpages += arr[i]   # Give book to current student
            else:
                count += 1            # Allocate new student
                currpages = arr[i]    # Start new student's pages
        
        return count  # Total students required

    def findPages(self, n, arr, m):
        if m > n:
            return -1   # More students than books
        
        maxi = max(arr)     # Largest single book
        high = sum(arr)     # Total pages of all books
        
        low = maxi
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2   # Binary search mid
            
            x = self.noofstudents(n, arr, mid)
            
            if x <= m:
                ans = mid         # Possible answer
                high = mid - 1    # Try smaller maximum
            else:
                low = mid + 1     # Increase pages
        
        return ans