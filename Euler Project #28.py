import time
start = time.time()

def Number_spiral_diagonals(n):
    Numberspiraldiagonals = [1]
    for x in range(2,n):
        Numberspiraldiagonals.append((4*(x**2)-10*(x-1)-3)+(4*(x**2)-8*(x-1)-3)+(4*(x**2)-6*(x-1)-3)+(4*(x**2)-4*(x-1)-3))
    print(sum(Numberspiraldiagonals))

Number_spiral_diagonals(502)

end = time.time()
print(end - start)



