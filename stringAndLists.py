words = "It's thanksgiving day. It's my birthday,too!"
words=words.replace("day","month")
print(words)
x = [2,54,-2,7,12,98]
min =x[0]
max =x[0]
for val in x:
    if val > max:
        max=val
    if val < min:
        min=val
print "Max is:", max, "Min is:", min

y = ["hello",2,54,-2,7,12,98,"world"]

print "first word: ", y[0], "last word:", y[len(y)-1] 

li = [19,2,54,-2,7,12,98,32,10,-3,6]
li.sort()
print(li)