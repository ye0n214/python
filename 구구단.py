for i in range(2, 10):
    print(f"# {i}단 #",end="\t")
print()

for j in range(1, 10):
    for i in range(2, 10):
        print(f"{i}X {j:1d}={i*j:2d}",end="\t")
    print()