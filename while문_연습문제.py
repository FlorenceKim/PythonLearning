sum = 0
a=0
while a<=100:
    sum = sum+a
    a= a+1   
print(sum)

a =1
while a<=1000:
    a = a+1
    if a % 3==1: continue
    if a % 3==2: continue
    print(a)
    
a = [20,55,67,82,45,33,90,87,100,25]
result = 0

while a:
    mark = a.pop()
    if mark >= 50:
        result +=mark

print(result)

