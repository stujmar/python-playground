t = ("Norway", 17.71, 5)
print(t[0])

for item in t:
    print(item)


singleTuple = ("lone item",) #trailing comma
emptyTuple = () 

print(singleTuple[0])

#tuple unpacking. a little like destructuring.

def minmax(items):
    return min(items), max(items) #comma separates multiple return values?

x = minmax([3,54,72,2,545,7,3])
print(x)

a = 'jelly'
b = 'bean'
a, b = b, a
print(a)
print(b)

#in operator