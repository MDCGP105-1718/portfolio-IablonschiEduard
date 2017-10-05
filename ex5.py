n = 99
for n in range(99,-1,-1):
    if n == 0:
        print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall…")
    else:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down, pass it around, {n-1} bottles of beer on the wall…")
