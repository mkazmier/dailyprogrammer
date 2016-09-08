"""Challenge #223 [Easy]
   https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/?"""

def garland(word):
   for i in range(len(word)//2+1):
      if word.startswith(word[len(word)//2+i:]):
         return len(word[len(word)//2+i:])
   return 0

print("garland('programmer') -> {}".format(garland('programmer')))
print("garland('ceramic') -> {}".format(garland('ceramic')))
print("garland('onion') -> {}".format(garland('onion')))
print("garland('alfalfa') -> {}".format(garland('alfalfa')))
