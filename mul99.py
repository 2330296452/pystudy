i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i:2d}", end="  ")
        j += 1
    print()
    i += 1

print()

for i in range(1, 10):
    for j in range(1, i + 1):
        # print("%d * %d = %-2d" % (j, i, j * i), end="  ")
        print(f"{j} * {i} = {j * i:2d}", end="  ")
    print()

print()

i = 1
while i < 10:
    j = 1
    while j < 10:
        if j > i:
            break
        print(f"{j} * {i} = {j * i:2d}", end="  ")
        j += 1
    i += 1
    print()

print()

i = 1
while i < 10:
    j = 0
    while j < 10:
        j += 1
        if j > i:
            continue
        print(f"{j} * {i} = {j * i:2d}", end="  ")
    i += 1
    print()
