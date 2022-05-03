sent = input("введите предложение")
sent1 = sent.split()
a = set(sent1)
print(a)
for a in sent1:
    print(a[0:10])
