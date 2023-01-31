# Valid Anagram

def isAnagram(s: str, t: str) -> bool:
    x = []
    y = []

    for i in range(0, len(s)):
        x.append(s[i])

    for i in range(0, len(t)):
        y.append(t[i]) 

    # convert into tuple
    x = tuple(x)
    y = tuple(y)

    #print(x)
    #print(y)

    sorted_x = sorted(x)
    sorted_y = sorted(y)

    print(sorted_x)
    print(sorted_y)

    if len(x) == len(y):
        for i in range(0, len(x)):
            if sorted_x[i] != sorted_y[i]:
                print(sorted_x[i])
                print(sorted_y[i])
                return False
        return True
            


    else:
        return False
   


print(isAnagram('anagram', 'nagaram'))


