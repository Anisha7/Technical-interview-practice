
# "apple" --> false
# "cat" --> true

# idea 1: use set - if already in set: return false, otherwise add to set
# idea 2: use counter - using a dictionary
# idea 3: 2 for loops - first for loop starts at index 1, second loop does all items after it

def isUniqueBruteForce(s):
    # Space: O(1)
    # create two for loops
    for i in range(len(s)): # Time: O(N) * O(N-1) --> O(N**2) 
        for j in range(i+1, len(s)): # Time: O(N-1)
            if (s[i] == s[j]):
                return False
            
    return True
    
print(isUniqueBruteForce("apple") )
print(isUniqueBruteForce("cat"))

def isUnique(s):
    # create an empty set 
    seen = set() # Space: O(N)
    # loop through the string 
    for letter in s: # Time: O(N)
        if letter in seen: 
            return False 
        else: 
            seen.add(letter)
    return True

print(isUnique('dog'))
print(isUnique('tree'))