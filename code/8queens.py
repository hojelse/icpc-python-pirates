B = [[False]*8 for i in range(8)]
Valid = True
Count = 0

for (r,s) in [(i,input()) for i in range(8)]:
    if not Valid: break
    for i in range(len(s)):
        if s[i] == '*':
            Count += 1
            if B[r][i]:
                Valid = False
                break
            for c in range(8): 
                B[c][i] = True
                B[r][c] = True
            for c in range(8):
                if r+c < len(B): 
                    if i+c < len(B[r+c]): B[r+c][i+c] = True
                    if i-c >= 0: B[r+c][i-c] = True

if Valid and Count == 8: print('valid')
else: print('invalid')