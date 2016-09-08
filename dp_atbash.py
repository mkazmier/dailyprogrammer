"""Challenge #254 [Easy] Atbash Cipher
   https://www.reddit.com/r/dailyprogrammer/comments/45w6ad/20160216_challenge_254_easy_atbash_cipher/?"""

msg = input('Enter the message to encrypt: ')
alph = 'abcdefghijklmnopqrstuvwxyz'
cipher = dict(zip(alph, reversed(alph)))
enc = []
for c in list(msg):
   enc.append(cipher.get(c, c))
print(''.join(enc))
