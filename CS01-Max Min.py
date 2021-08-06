nub = int(input())
list = []
for i in range(nub):
    num = input()
    if num == "":break
    list.append(int(num))
print(list)
print(min(list))
print(max(list))