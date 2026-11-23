class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for letter in s:
            if letter.isalnum():
                clean = clean + letter.lower()

        left = 0
        right = len(clean)-1
        while left<right:
            if clean[left] != clean[right]:
                return False

            left +=1
            right -=1
        return True
