#https://projecteuler.net/problem=1
#Multiples of 3 and 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#it's not explicitly stated but the issue here seems to be one of "collision" i.e - 15 is both a multiple of 3 and 5, so you want to only include it once.

#3 loop
threetimes=0
total=0
print("starting")

while threetimes<1000:
    threetimes+=3
    if threetimes%5!=0:
        total+=threetimes

#5 loop
fives=0
while fives+5<1000:
    total+=fives
    fives+=5
print("final: "+str(total))
