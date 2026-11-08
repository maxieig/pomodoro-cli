num=5
total=0
while num>0:
    if num//2==0:
        total=total+(num*2)
    else:
        total=total-num
    num=num-1
print(num,"\t",total)