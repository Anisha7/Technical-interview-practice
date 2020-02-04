# Problem 1
# Given an array a of n numbers and a target value t, 
# find two numbers whose sum is t.
def twosum(arr, t):
    # Time: O(nlogn), Space: O(1)
    arr.sort()
    i = 0
    j = len(arr) - 1
    while (i != j):
        s = arr[i] + arr[j]
        if (s == t):
            return [arr[i], arr[j]]
        elif (s > t):
            j -= 1
        else:
            i += 1
    return None

# Problem 2
# Given an array a of n numbers and a count k 
# find the k largest values in the array a.
def kvalues(arr, t):
    # Time: O(nlogn) Space: O(1)
    arr.sort()
    return arr[len(arr)-t:]

# Problem 3
# Given two arrays a and b of numbers and a target value t, 
# find a number from each array whose sum is closest to t.
def closerSum(curr, given, t):
    if (abs(t-curr[0]) > abs(t-given[0])):
        return 0
    if (curr[0] > given[0]):
        return -1
    return 1

def arrsum(a1, a2, t):
    a1.sort()
    a2.sort()
    result = (0, -1, -1)

    for i in range(0, len(a1)):
        for j in range(0, len(a2)):
            s = a1[i] + a2[j] 
            given = (s, a1[i], a2[j])
            closerEval = closerSum(result, given, t)
            if (closerEval == 0):
                result = given
            # Added for optimization
            if (closerEval == 1):
                break
    return [result[1], result[2]]

def test():
    print("Testing Problem 1...")
    assert(set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {3, 7} or set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {6, 4} or set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {8, 2})
    assert(set(twosum([10,4,13,2,11,5], 7)) == {2, 5})
    assert(twosum([10,4,13,2,11,5], 200) == None)
    print("Passed.")
    print("Testing Problem 2...")
    assert(set(kvalues([5, 1, 3, 6, 8, 2, 4, 7], 3)) == {6, 8, 7})
    print("Passed.")
    print("Testing Problem 3...")
    assert(set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {13, 6} or set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {4, 17} or set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {5, 14})
    print("Passed.")

if __name__ == "__main__":
    test()