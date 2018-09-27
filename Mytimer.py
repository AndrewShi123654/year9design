'''
Mytimer.py - a program to test the speed of your computer
original coding, sep. 21, 2018

'''




# import timeit module
# only import the function required, speed up code
from timeit import default_timer as timer

#definr the function called mytimer
def mytimer():

	start = timer()
    print(start)
#loop statement	
	for i in range(1000000):
		print(i)
		
		end=timer()
        print(end)
		
		print(end-start)

#envoking or calling the function"mytimer"		
mytimer()