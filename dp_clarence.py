"""Challenge #259 [Easy] Clarence the Slow Typist
   https://www.reddit.com/r/dailyprogrammer/comments/4bc3el/20160321_challenge_259_easy_clarence_the_slow/?"""


from math import sqrt

addr = list(input('Enter address: '))
dist = lambda r1, c1, r2, c2: sqrt((r1-r2)**2+(c1-c2)**2)
keys = list('123456789.0')
coords =  [(r,c) for r in range(1,5) for c in range(1,4)]
keypad = dict(zip(keys, coords))

total = 0
for n,m in zip(addr, addr[1:]):
   total += dist(*keypad[n], *keypad[m])
print("The total distance is: %.2f cm" % total)
