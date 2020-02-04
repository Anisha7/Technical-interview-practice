# Problem 1
# Given an array a of n numbers and a target value t, 
# find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  =>  
# [3, 7] or [6, 4] or [8, 2]
def twosum(arr, t):
    # Time: O(nlogn), Space: O(1)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == t):
                return [arr[i], arr[j]]
    return None

# Problem 2
# Given an array a of n numbers and a count k 
# find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  =>  
# [6, 8, 7]
def kvalues(arr, t):
    # Time: O(n*tlogt) Space: O(t)
    result = [-1]*t
    for i in range(len(arr)):
        if (arr[i] > result[0] or result[0] == -1):
            result.append(arr[i])
            result.sort()
            result.pop(0)
    return result

# Problem 3
# Given two arrays a and b of numbers and a target value t, 
# find a number from each array whose sum is closest to t.
def arrsum(a1, a2, t):
    pass

def test():
    print("Testing Problem 1...")
    assert(set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {3, 7} or set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {6, 4} or set(twosum([5, 3, 6, 8, 2, 4, 7], 10)) == {8, 2})
    assert(set(twosum([10,4,13,2,11,5], 7)) == {2, 5})
    assert(twosum([10,4,13,2,11,5], 200) == None)
    print("Passed.")
    print("Testing Problem 2...")
    print(kvalues([5, 1, 3, 6, 8, 2, 4, 7], 3))
    assert(set(kvalues([5, 1, 3, 6, 8, 2, 4, 7], 3)) == {6, 8, 7})
    print("Passed.")
    print("Testing Problem 3...")
    assert(set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {13, 6} or set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {4, 17} or set(arrsum([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20)) == {5, 14})
    print("Passed.")

if __name__ == "__main__":
    test()