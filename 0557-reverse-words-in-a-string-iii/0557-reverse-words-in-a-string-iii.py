class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_words =[]
        for i in words:
           reversed_words.append(i[::-1])
        return " ".join(reversed_words)