#Input a number
num = int(input("Enter a number : "))
t = num
numLen = 0
#iterate the loop
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numlen>=4: #condition 1 
    numLen = int(numLen/2)
    chk = 0
    while num>0: #iterate loop
        rem = num%10
        if chk==numLen: #nested condition 1 
            midOne = rem
        elif chk==(numLen-1):   
            midtwo = rem
        num = int(numLen-1)
        chk = chk+1
    prod = midOne*midtwo #product of middle digits 
    