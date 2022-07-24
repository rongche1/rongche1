g = [1,2,3,4,5,6,7,8,9,10]
g.sort()
biggest = 0
list_biggest = []
for i in g:
    if (i > biggest) and (len(list_biggest) < 4):
        list_biggest.append(i)
        biggest = i
    elif (i > biggest) and (len(list_biggest) >= 4):
        list_biggest.remove(list_biggest[0])
        list_biggest.append(i)
        biggest = i
    else:
        continue
print(list_biggest)  