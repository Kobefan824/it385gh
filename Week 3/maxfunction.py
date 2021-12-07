#!/usr/bin/python3
def maxOfTwoNumbers(a, b):
    # code to do
    if a > b:
        max = a
    else:
        max = b

    return max

def main():
    n1 = 3
    n2 = 4
    maximum = maxOfTwoNumbers(n1, n2)
    print("maximum of", n1, "and", n2, "is", maximum )

main()
