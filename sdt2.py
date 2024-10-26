s = str(input())
ans = ''
for i in range(len(s)):
    if s[i] not in ['a', 'e', 'u', 'i', 'o', 'A', 'E', "I", 'O', 'U']:
        ans+=s[i]
print(ans)
