#return True if sum of any two num in list equals key
num=[]
key=25
m=[]
n=int(input())
for x in range(n):
    num.append(int(input()))
for x in range(n):
    if key-num[x] in num:
        print(True)
        break
print(None)