class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        # remove useless characters
        for char in s:
            if char.isalnum(): # if character is alpha-numerical
        # converting to lowercase
                newStr += char.lower()
        # reversing the string
        return newStr == newStr[::-1]
        # check for equality