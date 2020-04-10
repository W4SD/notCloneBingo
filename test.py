rows = range(15)
cols = range(5)
hits = (2, 7, 12)

for r in rows:
    for c in cols:
        if r in hits and c is 3:
            print("jee")
        else:
            print(f" row: {r}, col: {c}")
