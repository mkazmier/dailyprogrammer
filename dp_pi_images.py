"""Challenge #225 [Intermediate] Estimating pi from images of circles
   https://www.reddit.com/r/dailyprogrammer/comments/3f0hzk/20150729_challenge_225_intermediate_estimating_pi/?"""

# NOTE: only works with Python 2, as PyPNG has not been ported to Python 3 yet.

from __future__ import division
import png
from sys import argv, exit

def find_black(img_data):
   for i, r in enumerate(img_data):
      if min(r) == 0:
         return i

def get_radius(img_data):
   return (len(img_data) - (find_black(img_data[::-1]) + find_black(img_data) + 1)) / 2 

def get_area(img_data):
   return sum(r.count(0) for r in img_data) / 3


try:
   with open(argv[1], 'r') as img:
      r = png.Reader(img)
      img_data = list(r.read()[2])

except IndexError:     
   print("Usage: {} <image_file>".format(argv[0]))
   exit(0)

pi_est = get_area(img_data) / get_radius(img_data) ** 2

print("The estimated value of pi is: {}".format(pi_est)) 
