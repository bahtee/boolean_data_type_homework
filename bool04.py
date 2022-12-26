def main(a):
    """
    check the following statement "The variable "a" is negative"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    a = a < 0
    return bool(a)
print(main(-3))    