def main(a):
    """
    check the following statement "The variable "a" is an odd number"
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    a = a % 2
    return bool(a != 0)
print(main(8))    