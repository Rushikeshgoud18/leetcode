class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        left = 0
        right = len(s)-1

        while left<right:
            if s[left] != s[right]:
                skip_left = s[left + 1:right+1]
                skip_right = s[left:right]
                return is_palindrome(skip_left) or is_palindrome(skip_right)

            left +=1
            right -=1

        return True


       

        