class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_num = ""
        for i in s:
            if i.isalnum():
                a_num += i.lower()
        return a_num == a_num[::-1]