a = input("введите число или stop")
list=[]
while a!="stop":
    list.append(a)
    a = input("введите число или stop")
print (list)
for i in range(1,len(list),2):
    list[i-1],list[i]=list[i],list[i-1]
print(list)
