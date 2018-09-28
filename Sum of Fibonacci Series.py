n = int(input('please enter a number greater than 0 '))
sum = 0
for i in range(n):
    if i > 0:
        pair = i + (i-1)
        for a in range(n-1):
            lastpair = a + (a-1)
        #print(i, (i-1), lastpair, pair)
sum = (pair + lastpair)
print(sum)
        
