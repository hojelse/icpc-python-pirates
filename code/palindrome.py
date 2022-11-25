def isPalindrome(s):
  offset = 1 if len(s) % 2 == 1 else 0
  return s[len(s)//2-1::-1] == s[len(s)//2+offset:]