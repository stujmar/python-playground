import timeit

def test(number):
    count = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            count += num
    return count

def test_two(number):
    result = []
    for num in range(number):
        if num % 5 == 0 or num % 3 == 0:
            result.append(num)
    return sum(result)

print("First test: ", timeit.timeit( "test(100)", setup="from __main__ import test"))
print("Second test: ", timeit.timeit( "test_two(100)", setup="from __main__ import test_two"))

print("First test: ", timeit.timeit( "test(1000)", setup="from __main__ import test"))
print("Second test: ", timeit.timeit( "test_two(1000)", setup="from __main__ import test_two"))