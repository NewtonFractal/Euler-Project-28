import time
start = time.time()

def Number_spiral_diagonals(n):
    Numberspiraldiagonals = [1]
    for x in range(2,n):
        Numberspiraldiagonals.append((16*(x**2)-28*(x-1)-12))
    print(sum(Numberspiraldiagonals))

Number_spiral_diagonals(502)

end = time.time()
print(end - start)
