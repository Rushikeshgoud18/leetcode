class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxcandies= max(candies)
        ans=[]
        for i in candies:
            if (i+extraCandies)>= maxcandies:
                ans.append(True)
            else:
                ans.append(False)


        return ans