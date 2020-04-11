# Towers of Hanoi

# Given 3 pegs (A,B,C) and n disks, 
# where each disk is a different size,
# and are initially on peg A in order 
# of decreasing size (bottom to top),
# move all disks to peg B in the same order

# rules:
# You may only move one disk at a time.
# No disk may ever rest atop a smaller disk.
# For ex. if disk 3 is on a peg, all disks 
# below disk 3 must have numbers larger than 3

# conceptually: slow solution using arrays
def solveHanoiArray(n):
    A = [*range(n, 0, -1)] # EX. [3, 2, 1] if n = 3
    B = []
    C = []
    print(f"Input: start - {A}, end - {B}, temp - {C}")
    solveHanoiArrayHelper(n, A, B, C)
    print(f"Result: start - {A}, end - {B}, temp - {C}")
    
def solveHanoiArrayHelper(n, start, end, temp):
    # base case: no disks to move
    if (n == 0 or len(start) == 0):
        return
    solveHanoiArrayHelper(n-1, start, temp, end)
    end.append(start.pop())
    solveHanoiArrayHelper(n-1, temp, end, start)

solveHanoiArray(3)
solveHanoiArray(10)


# Now lets solve it by printing the steps Ex. A to B or B to C
def solveHanoiDirections(n):
    return solveHanoiDirectionsHelper(n, 'A', 'B', 'C')
    
def solveHanoiDirectionsHelper(n, start, end, temp):
    # base case: no disks to move
    # base case: no disks to move
    if (n == 0 or len(start) == 0):
        return

    solveHanoiDirectionsHelper(n-1, start, temp, end)
    print(f"Move {start} to {end}")
    solveHanoiDirectionsHelper(n-1, temp, end, start)

print("Moves with 3 disks: ")
solveHanoiDirections(3)
# print("Moves with 10 disks: ")
# solveHanoiDirections(10)

# Now lets solve it by returning how many steps it will take
# Optimized solution
def solveHanoi(n):
    return solveHanoiHelper(n, 'A', 'B', 'C')
    
def solveHanoiHelper(n, start, end, temp, memo={}):
    # base case:
    if (n < 2):
        return  n
    if (n == 2):
        return 3
    if (n in memo):
        return memo[n]

    result = 1 + solveHanoiHelper(n-1, start, temp, end, memo) + solveHanoiHelper(n-1, temp, end, start, memo)
    memo[n] = result
    return result

print(solveHanoi(3)) # 7
print(solveHanoi(4)) # 15
print(solveHanoi(1000))

