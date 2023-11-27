tt = 0
for i in range(1, 101):
    for c in range(1, 101):
        if i%c == 0:
            tt+=1
    if tt==2:
        print(i)
    tt = 0