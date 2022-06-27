L = input()
H = input()
ans = 0
for idx, h in enumerate(H):
    ans += (ord(h)-96) * (31**idx)
ans = ans % 1234567891
print(ans)
