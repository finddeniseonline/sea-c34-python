# import sys
# sys.setrecursionlimit(100000)
# Session 02 Task 4

print("\n")
print("# --------------------------------------------------------#")
print("#             Session 02 Task 4                           #")
print("#                                                         #")
print("#        Fibonnaci and Lucas Sequences                    #")
print("# --------------------------------------------------------#")


print("\nThis is the Fibonnaci sequence function")


def fib(n):  # Fibonnaci sequence
    if n < 0:
        return None
    elif n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#  Another version iterative

# a = b = 1
# if n <= 2:
#    return b
# for i in range(2, n+1):
#    a, b = b, a + b
# return b

# Version 2: recursion
# if n < 2:
#     return 1L
# return fibonacci(n-1) + fibonacci(n-2)
# print fib(13)


input("\nPress Enter to continue...\n")

print("This is the Lucas sequence function")


def lucas(n):  # Function to return the nth lucas number.
    # if n < 0:
    #     return None
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

# print lucas(4)

# Recursive version
# return lucas(n-1) + lucas(n-2)

input("\nPress Enter to continue...\n")

print("This is the sum series function")


def sum_series(n, num=0):
    if n == 0:
        return num
    elif n == 1:
        return 1
    else:
        return sum_series(n-1, num) + sum_series(n-2, num)


# To see Ackerman number example uncomment code
# below as this is a recursive function.

# raw_input("\nPress Enter to continue...\n")

# print "This is the Ackerman sequence function..."
# print "just for $&%! and giggles"

# def A(m, n):  # Ackerman numbers
#    if m == 0:
#       return n + 1
#    elif m > 0 and n == 0:
#        return A(m - 1, 1)
#    else:
#        return A(m - 1, A(m, n - 1))
# A(5, 6)

print("\nrunning some asserts\n")
if __name__ == "__main__":  # perform some tests

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    # assert fib(6) == 8
    # assert fib(7) == 13
    # assert lucas(4) == 7
    # assert lucas(11) == 18
    # assert lucas(29) == 47
    print(u"Fibanacci tests pass")

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    print(u"lucas tests pass")

    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    print(u"sum_series for Fibanacci tests pass")

    assert sum_series(0, 2) == 2
    assert sum_series(1, 2) == 1
    assert sum_series(2, 2) == 3
    assert sum_series(3, 2) == 4
    print(u"sum series for Lucas tests pass")
