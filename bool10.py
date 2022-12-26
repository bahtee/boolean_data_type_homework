import math
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    a = math.sqrt(a)
    a = a % 1
    

    return a == 0
print(main(121))    