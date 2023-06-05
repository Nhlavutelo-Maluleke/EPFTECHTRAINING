a = 600851475143
b = 2

while a  != 1:
    remainder =a%b
    if remainder == 0:
        a = a/b 
        print (b)

    else:
        b +=1