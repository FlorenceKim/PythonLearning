money = 5000
card = False

if money >=4000 or card:
    print(" Take Texi")
else:
    print("you cannot take taxi")
    
a = [1,9,23,46]

if 23 in a:
    print("당첨!")
else:
    print("꽝")
    

num = 98

if num%2 == 0:
    print("짝수")
else:
    print("홀수")
    
a = "f,70"
b = "m,45"
mf, num = a.split(",")
isodd=int(num) % 2

if mf == "m" and isodd:
    print ("A반")
elif mf == "m" and not isodd:
    print ("B반")
elif mf == "f" and isodd:
    print ("C반")
elif mf== "f" and not isodd:
    print("D반")
    
mf, num = b.split(",")
isodd=int(num)%2
    
if mf == "m" and isodd:
    print ("A반")
elif mf == "m" and not isodd:
    print ("B반")
elif mf == "f" and isodd:
    print ("C반")
elif mf== "f" and not isodd:
    print("D반")
    