thislist = ['5','10','15','20','25','50','20']
print(thislist)
for i in range(len(thislist)):
    print
    if (thislist[i] == '20'):
        thislist[i] = '200'
print(thislist)