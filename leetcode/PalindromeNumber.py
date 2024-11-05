# Palindrome Number

# def isPalindrome() ->bool:
#     x=-124
#     # if x<0:
#     #     return False
#     input=121
#     seprated_digit=[int(digit) for digit in str(x)]
#     print(seprated_digit)
#     reversed_digit=seprated_digit[::-1]
#     print(reversed_digit)
#     if reversed_digit== seprated_digit:
#         return True
# isPalindrome()    
class Solution(object):
    @staticmethod
    def isPalindrome(x):
        s = str(x)
        return s == s[::-1]
print(Solution.isPalindrome(122))
