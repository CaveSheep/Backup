import time
import os

frameList = ['''
p       O      q
L__   __|__   _J
   \ /  |  \ /
    U   |   U
        |
       / \
      /   \
     /     \
''',
'''
p       O       q
L___^___|___^___J
    u   |   u
        |
        |
       / \
      /   \
     /     \
 ''']

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.2)
		os.system("cls")
